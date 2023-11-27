import tkinter as tk
from tkinter import simpledialog, messagebox
from Model.Emprestimo import Emprestimo
from Model.TelaMenu import TelaMenu
from Model.Usuario import Usuario


class TelaMenuBibliotecario(TelaMenu):
    def __init__(self, usuario):
        super().__init__(usuario)
        self.setup_deletar_emprestimo_button()
        self.setup_cadastrar_bibliotecario_button()

    def setup_deletar_emprestimo_button(self):
        estilos_btn = {'bg': "#3498DB", 'fg': "white", 'width': 15, 'font': ('Helvetica', 12)}

        btn_deletar_emprestimo = tk.Button(self.central_space, text="Deletar Empréstimo",
                                           command=self.deletar_emprestimo, **estilos_btn)
        btn_deletar_emprestimo.pack(side=tk.TOP, pady=(0, 10))

    def setup_cadastrar_bibliotecario_button(self):
        estilos_btn = {'bg': "#3498DB", 'fg': "white", 'width': 15, 'font': ('Helvetica', 12)}

        btn_cadastrar_bibliotecario = tk.Button(self.central_space, text="Cad. Bibliotecario",
                                                command=self.cadastrar_bibliotecario, **estilos_btn)
        btn_cadastrar_bibliotecario.pack(side=tk.TOP, pady=(0, 10))

    def deletar_emprestimo(self):
        codigo_emprestimo = simpledialog.askstring("Deletar Empréstimo",
                                                   "Digite o código do empréstimo a ser deletado:")

        # verifica se o empréstimo existe
        if not self.emprestimo_existe(codigo_emprestimo):
            messagebox.showinfo("Aviso", "Este empréstimo não existe.")
            return

        # confirmação do usuário
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja deletar este empréstimo?")

        if resposta:
            # remove o empréstimo do arquivo
            emprestimos = Emprestimo.ler_emprestimos_do_arquivo()
            emprestimos = [e for e in emprestimos if e.codigo != codigo_emprestimo]
            Emprestimo.salvar_emprestimos_no_arquivo(emprestimos)

            messagebox.showinfo("Sucesso", "Empréstimo deletado com sucesso.")
            self.listar_emprestimos()

    @staticmethod
    def emprestimo_existe(codigo_emprestimo):
        emprestimos = Emprestimo.ler_emprestimos_do_arquivo()
        return any(emprestimo.codigo == codigo_emprestimo for emprestimo in emprestimos)

    def cadastrar_bibliotecario(self):
        novo_bibliotecario = Usuario()

        # pde informações para o novo bibliotecário
        nome_bibliotecario = simpledialog.askstring("Cadastro de Bibliotecário", "Digite o nome:")
        login_bibliotecario = simpledialog.askstring("Cadastro de Bibliotecário", "Digite o login:")
        senha_bibliotecario = simpledialog.askstring("Cadastro de Bibliotecário", "Digite a senha:")

        # verificação de campos não prenchidos
        if not nome_bibliotecario or not login_bibliotecario or not senha_bibliotecario:
            messagebox.showerror("Erro no Cadastro", "Todos os campos devem ser preenchidos.")
            return

        # login já existe
        if login_bibliotecario in self.usuario.getUsuarios():
            messagebox.showerror("Erro no Cadastro", "Login já existe. Escolha outro.")
            return

        # bter o próximo código de usuário
        codigo_usuario = self.obter_proximo_codigo_usuario()

        # Preencher outras informações do bibliotecário
        novo_bibliotecario.instanciar_usr(codigo_usuario, nome_bibliotecario, "Bibliotecario")
        novo_bibliotecario.set_login(login_bibliotecario)
        novo_bibliotecario.set_senha(senha_bibliotecario)

        # adicionando o novo bibliotecario ao arquivo usuario.txt
        with open('txt/usuarios.txt', 'a') as arquivo_usuarios:
            arquivo_usuarios.write(f"{novo_bibliotecario.get_codigo()},"
                                   f"{novo_bibliotecario.get_nome()},"
                                   f"{novo_bibliotecario.get_tipo()},"
                                   f"{novo_bibliotecario.get_login()},"
                                   f"{novo_bibliotecario.get_senha()}\n")

        messagebox.showinfo("Cadastro realizado", "Bibliotecário cadastrado com sucesso.")

    @staticmethod
    def obter_proximo_codigo_usuario():
        # lê o arquivo de usuários e identifica o último código da última linha do txt
        with open('txt/usuarios.txt', 'r') as arquivo_usuarios:
            linhas = arquivo_usuarios.readlines()
            if linhas:
                ultimo_codigo = int(linhas[-1].split(',')[0])
                proximo_codigo = ultimo_codigo + 1
            else:
                proximo_codigo = 1

        return proximo_codigo
