import tkinter as tk

from Model.Livro import Livro
from Model.Emprestimo import Emprestimo


class TelaMenu:
    def __init__(self, usuario):
        self.usuario = usuario

        self.root = tk.Tk()
        self.root.title("Sistema Bibliotecário - Menu")

        # Define o tamanho da janela
        self.root.geometry("800x400")

        # Coluna esquerda (cor sólida)
        left_frame = tk.Frame(self.root, width=250, height=400, bg="black")
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Frame(left_frame, height=20, bg="black").pack(side=tk.TOP)

        central_space = tk.Frame(left_frame, height=200, bg="black")
        central_space.pack(side=tk.TOP)

        # Coluna direita (resultados)
        right_frame = tk.Frame(self.root, padx=20, pady=20)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        label_bem_vindo = tk.Label(right_frame, text=f"Bem-vindo, {usuario.get_nome()}!",
                                   font=('Helvetica', 12, 'bold'))
        label_bem_vindo.grid(row=0, column=0, pady=(0, 10))

        # Widget de texto maior para exibir informações
        self.texto_resultado = tk.Text(right_frame, width=80, height=20)  # Ajustei a altura
        self.texto_resultado.grid(row=1, column=0, pady=(0, 10))

        btn_listar_livros = tk.Button(central_space, text="Listar Livros", command=self.listar_livros)
        btn_listar_livros.pack(side=tk.TOP, pady=(20, 10))  # Ajustei a altura

        btn_listar_emprestimos = tk.Button(central_space, text="Listar Empréstimos",
                                           command=self.listar_emprestimos)
        btn_listar_emprestimos.pack(side=tk.TOP, pady=(0, 10))

        btn_sobre = tk.Button(central_space, text="Sobre", command=self.mostrar_sobre)
        btn_sobre.pack(side=tk.TOP, pady=(0, 10))

        btn_sair = tk.Button(central_space, text="Sair", command=self.sair)
        btn_sair.pack(side=tk.TOP, pady=(0, 10))

        self.root.mainloop()

    def listar_livros(self):
        # Limpa o widget de texto antes de listar os livros
        self.texto_resultado.delete(1.0, tk.END)

        # Lista os livros no widget de texto
        livros = Livro.ler_livros_do_arquivo()
        for livro in livros:
            info_livro = f"Código: {livro.codigo}, Título: {livro.titulo}, Autor: {livro.autor}\n"
            self.texto_resultado.insert(tk.END, info_livro)

    def listar_emprestimos(self):
        # Limpa o widget de texto antes de listar os empréstimos
        self.texto_resultado.delete(1.0, tk.END)

        # Lista os empréstimos no widget de texto
        emprestimos = Emprestimo.ler_emprestimos_do_arquivo()
        for emprestimo in emprestimos:
            info_emprestimo = (
                f"Código: {emprestimo.codigo}, Cliente: {emprestimo.cliente}, "
                f"Livro: {emprestimo.livro}, Data: {emprestimo.data}\n"
            )
            self.texto_resultado.insert(tk.END, info_emprestimo)

    def mostrar_sobre(self):
        # Limpa o widget de texto antes de exibir informações sobre o sistema
        self.texto_resultado.delete(1.0, tk.END)

        # Exibe informações sobre o sistema no widget de texto
        sobre_info = "Sistema Bibliotecário\nVersão 1.0\nDesenvolvido por [Seu Nome]\n"
        self.texto_resultado.insert(tk.END, sobre_info)

    def sair(self):
        self.root.destroy()


