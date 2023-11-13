import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from Model.TelaMenu import TelaMenu
from Model.Usuario import Usuario

class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bibliotecário - Login")
        self.root.geometry("600x400")

        self.setup_layout()

    def setup_layout(self):
        # Frame esquerdo com imagem redimensionada
        left_frame = tk.Frame(self.root, width=250, height=400, bg="#2C3E50")
        left_frame.grid(row=0, column=0)

        # Carrega e redimensiona a imagem
        original_image = Image.open("img/librateca-img.jpg")
        width, height = 250, 400
        resized_image = original_image.resize((width, height))
        photo = ImageTk.PhotoImage(resized_image)

        # Exibe a imagem
        label_image = tk.Label(left_frame, image=photo, bg="#2C3E50")
        label_image.image = photo
        label_image.pack(fill=tk.BOTH, expand=True)

        # Frame direito (área de login)
        right_frame = tk.Frame(self.root, padx=20, pady=20, bg="#ECF0F1")
        right_frame.grid(row=0, column=1, padx=50, pady=50)

        # Elementos da área de ‘login’
        label_login = tk.Label(right_frame, text="Login:", font=("Helvetica", 12), bg="#ECF0F1")
        label_login.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.entry_login = tk.Entry(right_frame, font=("Helvetica", 12))
        self.entry_login.grid(row=1, column=0, pady=(0, 10), padx=10, ipady=8)

        label_senha = tk.Label(right_frame, text="Senha:", font=("Helvetica", 12), bg="#ECF0F1")
        label_senha.grid(row=2, column=0, pady=(0, 10), sticky="w")

        self.entry_senha = tk.Entry(right_frame, show="*", font=("Helvetica", 12))
        self.entry_senha.grid(row=3, column=0, pady=(0, 10), padx=10, ipady=8)

        btn_entrar = tk.Button(right_frame, text="Entrar", command=self.validar_acesso, bg="#3498DB", fg="white", font=("Helvetica", 12))
        btn_entrar.grid(row=4, column=0, pady=(10, 0), ipady=8)

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