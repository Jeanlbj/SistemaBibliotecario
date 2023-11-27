import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from Model.TelaMenu import TelaMenu
from Model.TelaMenuBibliotecário import TelaMenuBibliotecario
from Model.Usuario import Usuario
from Model.TelaCadastro import TelaCadastro


class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bibliotecário - Login")
        self.root.geometry("600x400")

        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.configure('TEntry', font=('Helvetica', 12))

        self.tela_cadastro = None  # Inicialize o atributo aqui

        self.setup_layout()

    def setup_layout(self):
        # frame esquerdo com imagem
        left_frame = tk.Frame(self.root, width=250, height=400, bg="#2C3E50")
        left_frame.grid(row=0, column=0)

        # carregando e redimensionando imagem
        original_image = Image.open("img/librateca-img.jpg")
        width, height = 250, 400
        resized_image = original_image.resize((width, height))
        photo = ImageTk.PhotoImage(resized_image)

        # exibir imagem
        label_image = tk.Label(left_frame, image=photo, bg="#2C3E50")
        label_image.image = photo
        label_image.pack(fill=tk.BOTH, expand=True)

        # frame direito (login)
        right_frame = ttk.Frame(self.root, padding=(20, 20, 20, 20), style='TFrame')
        right_frame.grid(row=0, column=1, padx=50, pady=50, sticky="nsew")

        # elementos da área de login
        label_login = ttk.Label(right_frame, text="Login:", style='TLabel')
        label_login.grid(row=0, column=0, pady=(0, 10), sticky="w")

        entry_login = ttk.Entry(right_frame, font=("Helvetica", 12), style='TEntry')
        entry_login.grid(row=1, column=0, pady=(0, 10), padx=10, ipady=8)

        label_senha = ttk.Label(right_frame, text="Senha:", style='TLabel')
        label_senha.grid(row=2, column=0, pady=(0, 10), sticky="w")

        entry_senha = ttk.Entry(right_frame, show="*", font=("Helvetica", 12), style='TEntry')
        entry_senha.grid(row=3, column=0, pady=(0, 10), padx=10, ipady=8)

        btn_entrar = ttk.Button(right_frame, text="Entrar",
                                command=lambda: self.validar_acesso(entry_login.get(), entry_senha.get()),
                                style='TButton')
        btn_entrar.grid(row=4, column=0, pady=(10, 0), ipady=8)

        # Botão "Cadastrar" para abrir a tela de cadastro
        btn_cadastrar = ttk.Button(right_frame, text="Cadastrar", command=self.abrir_tela_cadastro, style='TButton')
        btn_cadastrar.grid(row=5, column=0, pady=(10, 0), ipady=8)

    def validar_acesso(self, login, senha):
        usuario = Usuario()
        usuario.set_login(login)
        usuario.set_senha(senha)

        if usuario.validar_acesso():
            messagebox.showinfo("Acesso Permitido", f"Bem-vindo(a) {usuario.get_nome()}!")

            if usuario.get_tipo() == 'Cliente':
                self.root.destroy()
                TelaMenu(usuario)
            elif usuario.get_tipo() == 'Bibliotecario':
                self.root.destroy()
                TelaMenuBibliotecario(usuario)
        else:
            messagebox.showerror("Acesso Negado", "Login ou senha inválidos")

    def abrir_tela_cadastro(self):
        self.tela_cadastro = TelaCadastro(self.root)
