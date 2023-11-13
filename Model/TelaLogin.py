import tkinter as tk
from tkinter import messagebox

from Model.TelaMenu import TelaMenu
from Model.Usuario import Usuario


class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bibliotecário - Login")

        # Coluna esquerda (cor sólida)
        left_frame = tk.Frame(root, width=200, height=400, bg="black")
        left_frame.grid(row=0, column=0)

        # Coluna direita (área de login)
        right_frame = tk.Frame(root, padx=20, pady=20)
        right_frame.grid(row=0, column=1, padx=50, pady=50)

        # Elementos da área de ‘login’
        label_login = tk.Label(right_frame, text="Login:")
        label_login.grid(row=0, column=0, pady=(0, 10))

        self.entry_login = tk.Entry(right_frame)
        self.entry_login.grid(row=1, column=0, pady=(0, 10))

        label_senha = tk.Label(right_frame, text="Senha:")
        label_senha.grid(row=2, column=0, pady=(0, 10))

        self.entry_senha = tk.Entry(right_frame, show="*")
        self.entry_senha.grid(row=3, column=0, pady=(0, 10))

        btn_entrar = tk.Button(right_frame, text="Entrar", command=self.validar_acesso)
        btn_entrar.grid(row=4, column=0)

    def validar_acesso(self):
        usuario = Usuario()
        usuario.set_login(self.entry_login.get())
        usuario.set_senha(self.entry_senha.get())

        if usuario.validar_acesso():
            messagebox.showinfo("Acesso Permitido", f"Bem-vindo(a) {usuario.get_nome()}!")
            self.root.destroy()
            TelaMenu(usuario)  # Chama a próxima tela passando o usuário autenticado
        else:
            messagebox.showerror("Acesso Negado", "Login ou senha inválidos")