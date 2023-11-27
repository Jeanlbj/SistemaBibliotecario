import tkinter as tk
from tkinter import messagebox, simpledialog
from Model.Livro import Livro
from Model.Emprestimo import Emprestimo
from datetime import datetime


class TelaMenu:
    def __init__(self, usuario):
        self.right_frame = None
        self.central_space = None
        self.left_frame = None

        self.texto_resultado = None
        self.usuario = usuario

        self.root = tk.Tk()
        self.root.title("Sistema Bibliotecário - Menu")
        self.root.geometry("800x400")
        self.root.configure(bg="#2C3E50")  # Cor de fundo para o tema escuro

        self.setup_layout()

    def setup_layout(self):
        # Frame esquerdo com cor sólida
        self.left_frame = tk.Frame(self.root, width=300, height=400, bg="#2C3E50")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Frame(self.left_frame, height=20, bg="#2C3E50").pack(side=tk.TOP)

        self.central_space = tk.Frame(self.left_frame, height=200, bg="#2C3E50")
        self.central_space.pack(side=tk.TOP)

        # Frame direito (resultados)
        self.right_frame = tk.Frame(self.root, padx=20, pady=20, bg="#ECF0F1")
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        label_bem_vindo = tk.Label(self.right_frame, text=f"Bem-vindo, {self.usuario.get_nome()}!",
                                   font=('Helvetica', 12, 'bold'), bg="#ECF0F1")
        label_bem_vindo.grid(row=0, column=0, pady=(0, 10), sticky="w")

        # Widget de texto maior para exibir informações
        self.texto_resultado = tk.Text(self.right_frame, width=80, height=20, bg="#ECF0F1", font=('Helvetica', 12))
        self.texto_resultado.grid(row=1, column=0, pady=(0, 10))

        # Botões com estilo
        estilos_btn = {'bg': "#3498DB", 'fg': "white", 'width': 15, 'font': ('Helvetica', 12)}

        btn_listar_livros = tk.Button(self.central_space, text="Listar Livros", command=self.listar_livros,
                                      **estilos_btn)
        btn_listar_livros.pack(side=tk.TOP, pady=(20, 10))

        btn_fazer_emprestimo = tk.Button(self.central_space, text="Fazer Empréstimo", command=self.fazer_emprestimo,
                                         **estilos_btn)
        btn_fazer_emprestimo.pack(side=tk.TOP, pady=(0, 10))

        btn_listar_emprestimos = tk.Button(self.central_space, text="Listar Empréstimos",
                                           command=self.listar_emprestimos, **estilos_btn)
        btn_listar_emprestimos.pack(side=tk.TOP, pady=(0, 10))

        btn_meus_emprestimos = tk.Button(self.central_space, text="Meus Empréstimos",
                                         command=self.listar_meus_emprestimos, **estilos_btn)
        btn_meus_emprestimos.pack(side=tk.TOP, pady=(0, 10))

        btn_sobre = tk.Button(self.central_space, text="Sobre", command=self.mostrar_sobre, **estilos_btn)
        btn_sobre.pack(side=tk.TOP, pady=(0, 10))

        btn_sair = tk.Button(self.central_space, text="Sair", command=self.sair, bg="#E74C3C", fg="white", width=15)
        btn_sair.pack(side=tk.TOP, pady=(0, 10))

    def listar_livros(self):
        self.texto_resultado.delete(1.0, tk.END)
        livros = Livro.ler_livros_do_arquivo()
        for livro in livros:
            info_livro = f"Código: {livro.codigo}, Título: {livro.titulo}, Autor: {livro.autor}\n"
            self.texto_resultado.insert(tk.END, info_livro)

    def listar_emprestimos(self):
        self.texto_resultado.delete(1.0, tk.END)
        emprestimos = Emprestimo.ler_emprestimos_do_arquivo()
        for emprestimo in emprestimos:
            info_emprestimo = (
                f"Código: {emprestimo.codigo}, Cliente: {emprestimo.cliente}, "
                f"Livro: {emprestimo.livro}, Data: {emprestimo.data}\n"
            )
            self.texto_resultado.insert(tk.END, info_emprestimo)

    def listar_meus_emprestimos(self):
        codigo_usuario = self.usuario.get_codigo()

        # Lê o arquivo de empréstimos
        emprestimos = Emprestimo.ler_emprestimos_do_arquivo()

        # filtra os empréstimos relacionados ao código do usuário
        meus_emprestimos = [e for e in emprestimos if e.cliente == codigo_usuario]

        # habilitar fazer edições no campo
        self.texto_resultado.config(state=tk.NORMAL)

        # limpa o campo antes de adicionar novos empréstimos
        self.texto_resultado.delete("1.0", tk.END)

        # printando empréstimos na campo de texto
        if meus_emprestimos:
            for emprestimo in meus_emprestimos:
                texto_emprestimo = f"Código: {emprestimo.codigo}, Livro: {emprestimo.livro}, Data: {emprestimo.data}\n"
                self.texto_resultado.insert(tk.END, texto_emprestimo)
        else:
            self.texto_resultado.insert(tk.END, "Você não possui empréstimos registrados.")

    @staticmethod
    def gerar_codigo_emprestimo():
        # gera um código de empréstimo único
        emprestimos = Emprestimo.ler_emprestimos_do_arquivo()
        codigo_emprestimo = str(int(datetime.timestamp(datetime.now())))

        # garantindo um código não repetido
        while any(emprestimo.codigo == codigo_emprestimo for emprestimo in emprestimos):
            codigo_emprestimo = str(int(datetime.timestamp(datetime.now())))

        return codigo_emprestimo

    def fazer_emprestimo(self):
        # Pergunta ao usuário o código do livro desejado
        codigo_livro = simpledialog.askstring("Fazer Empréstimo", "Digite o código do livro:")

        # Verifica se o livro existe no catálogo
        if not self.livro_existe_no_catalogo(codigo_livro):
            messagebox.showinfo("Aviso", "Este livro não está disponível no catálogo.")
            return

        # Verifica se o livro já está emprestado
        if self.livro_ja_emprestado(codigo_livro):
            messagebox.showinfo("Aviso", "Este livro já está emprestado.")
        else:
            # Cria um novo empréstimo
            emprestimo = Emprestimo(
                codigo=self.gerar_codigo_emprestimo(),
                cliente=self.usuario.get_codigo(),
                livro=codigo_livro,
                data=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

            # Adiciona o empréstimo ao arquivo
            Emprestimo.adicionar_emprestimo(emprestimo)

            messagebox.showinfo("Sucesso", "Empréstimo realizado com sucesso.")

    @staticmethod
    def livro_existe_no_catalogo(codigo_livro):
        livros = Livro.ler_livros_do_arquivo()
        for livro in livros:
            if livro.codigo == codigo_livro:
                return True
        return False

    @staticmethod
    def livro_ja_emprestado(codigo_livro):
        emprestimos = Emprestimo.ler_emprestimos_do_arquivo()
        for emprestimo in emprestimos:
            if emprestimo.livro == codigo_livro:
                return True
        return False

    def mostrar_sobre(self):
        self.texto_resultado.delete(1.0, tk.END)
        sobre_info = ("Fundada em 2023 por visionários alunos dos cursos de \n"
                      "Engenharia de Software e Sistemas de Informação do UniAcademia,\n"
                      "a Librateca é uma inovadora empresa de desenvolvimento de software.\n"
                      "Nossa missão é otimizar o gerenciamento de bibliotecas,\n"
                      "proporcionando uma experiência intuitiva e eficaz. E como visão, \n"
                      "buscamos ser líderes na transformação digital das bibliotecas, \n"
                      "oferecendo soluções inovadoras que atendam às necessidades \n"
                      "dinâmicas do mundo contemporâneo")
        self.texto_resultado.insert(tk.END, sobre_info)

    def sair(self):
        self.root.destroy()
