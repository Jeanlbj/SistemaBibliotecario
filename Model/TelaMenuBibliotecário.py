from tkinter import messagebox, simpledialog
from Model.Emprestimo import Emprestimo
from Model.TelaMenu import TelaMenu
import tkinter as tk


class TelaMenuBibliotecario(TelaMenu):
    def __init__(self, usuario):
        super().__init__(usuario)  # Chama o construtor da classe pai (TelaMenu)
        self.setup_deletar_emprestimo_button()

    def setup_deletar_emprestimo_button(self):
        btn_deletar_emprestimo = tk.Button(self.central_space, text="Deletar Empréstimo",
                                           command=self.deletar_emprestimo,
                                           bg="#3498DB", fg="white", width=15)
        btn_deletar_emprestimo.pack(side=tk.TOP, pady=(0, 10))

    @staticmethod
    def emprestimo_existe(codigo_emprestimo):
        emprestimos = Emprestimo.ler_emprestimos_do_arquivo()
        return any(emprestimo.codigo == codigo_emprestimo for emprestimo in emprestimos)

    def deletar_emprestimo(self):
        codigo_emprestimo = simpledialog.askstring("Deletar Empréstimo",
                                                   "Digite o código do empréstimo a ser deletado:")

        # Verifica se o empréstimo existe
        if not self.emprestimo_existe(codigo_emprestimo):
            messagebox.showinfo("Aviso", "Este empréstimo não existe.")
            return

        # Confirmação do usuário
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja deletar este empréstimo?")

        if resposta:
            # Remove o empréstimo do arquivo
            emprestimos = Emprestimo.ler_emprestimos_do_arquivo()
            emprestimos = [e for e in emprestimos if e.codigo != codigo_emprestimo]
            Emprestimo.salvar_emprestimos_no_arquivo(emprestimos)

            messagebox.showinfo("Sucesso", "Empréstimo deletado com sucesso.")
            self.listar_emprestimos()
