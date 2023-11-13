import tkinter as tk
from Model.Livro import Livro
from Model.Emprestimo import Emprestimo


class TelaMenu:
    def __init__(self, usuario):
        self.texto_resultado = None
        self.usuario = usuario

        self.root = tk.Tk()
        self.root.title("Sistema Bibliotecário - Menu")
        self.root.geometry("800x400")  # Ajustei a largura da janela

        self.setup_layout()

    def setup_layout(self):
        # Frame esquerdo com cor sólida
        left_frame = tk.Frame(self.root, width=300, height=400, bg="#2C3E50")  # Ajustei a largura
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Frame(left_frame, height=20, bg="#2C3E50").pack(side=tk.TOP)

        central_space = tk.Frame(left_frame, height=200, bg="#2C3E50")
        central_space.pack(side=tk.TOP)

        # Frame direito (resultados)
        right_frame = tk.Frame(self.root, padx=20, pady=20, bg="#ECF0F1")
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        label_bem_vindo = tk.Label(right_frame, text=f"Bem-vindo, {self.usuario.get_nome()}!",
                                   font=('Helvetica', 12, 'bold'), bg="#ECF0F1")
        label_bem_vindo.grid(row=0, column=0, pady=(0, 10), sticky="w")

        # Widget de texto maior para exibir informações
        self.texto_resultado = tk.Text(right_frame, width=80, height=20, bg="#ECF0F1")  # Ajustei a altura
        self.texto_resultado.grid(row=1, column=0, pady=(0, 10))

        btn_listar_livros = tk.Button(central_space, text="Listar Livros", command=self.listar_livros,
                                      bg="#3498DB", fg="white", width=15)  # Ajustei a largura
        btn_listar_livros.pack(side=tk.TOP, pady=(20, 10))

        btn_listar_emprestimos = tk.Button(central_space, text="Listar Empréstimos",
                                           command=self.listar_emprestimos, bg="#3498DB", fg="white", width=15)
        btn_listar_emprestimos.pack(side=tk.TOP, pady=(0, 10))

        btn_sobre = tk.Button(central_space, text="Sobre", command=self.mostrar_sobre, bg="#3498DB", fg="white",
                              width=15)
        btn_sobre.pack(side=tk.TOP, pady=(0, 10))

        btn_sair = tk.Button(central_space, text="Sair", command=self.sair, bg="#E74C3C", fg="white", width=15)
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

    def mostrar_sobre(self):
        self.texto_resultado.delete(1.0, tk.END)
        sobre_info = "Sistema Bibliotecário\nVersão 1.0\nDesenvolvido por [Seu Nome]\n"
        self.texto_resultado.insert(tk.END, sobre_info)

    def sair(self):
        self.root.destroy()
