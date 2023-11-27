import tkinter as tk
from tkinter import ttk, messagebox
from Model.Usuario import Usuario


class TelaCadastro:
    def __init__(self, master):
        self.entry_senha = None
        self.entry_login = None
        self.entry_nome = None

        self.master = master
        self.master.title("Cad. Usuário")
        self.master.geometry("600x400")

        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.configure('TEntry', font=('Helvetica', 12))

        # armazenar imagem
        self.photo = None

        self.setup_layout()

    def setup_layout(self):
        # Frame direito (área de cadastro)
        right_frame = tk.Frame(self.master, padx=20, pady=20, bg="#ECF0F1")
        right_frame.grid(row=0, column=1, sticky="nsew")

        # Configurar pesos das colunas
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

        # Adicionar Frame intermediário para centralizar os elementos
        center_frame = tk.Frame(right_frame, bg="#ECF0F1")
        center_frame.grid(row=0, column=0, sticky="nsew")

        # Elementos da área de cadastro
        label_nome = ttk.Label(center_frame, text="Nome:", style='TLabel')
        label_nome.grid(row=0, column=0, pady=(10, 5), padx=10, sticky="w")

        self.entry_nome = ttk.Entry(center_frame, font=("Helvetica", 12), style='TEntry')
        self.entry_nome.grid(row=1, column=0, pady=5, padx=10, ipady=8, sticky="ew")

        label_login = ttk.Label(center_frame, text="Login:", style='TLabel')
        label_login.grid(row=2, column=0, pady=(10, 5), padx=10, sticky="w")

        self.entry_login = ttk.Entry(center_frame, font=("Helvetica", 12), style='TEntry')
        self.entry_login.grid(row=3, column=0, pady=5, padx=10, ipady=8, sticky="ew")

        label_senha = ttk.Label(center_frame, text="Senha:", style='TLabel')
        label_senha.grid(row=4, column=0, pady=(10, 5), padx=10, sticky="w")

        self.entry_senha = ttk.Entry(center_frame, show="*", font=("Helvetica", 12), style='TEntry')
        self.entry_senha.grid(row=5, column=0, pady=5, padx=10, ipady=8, sticky="ew")

        btn_cadastrar = ttk.Button(center_frame, text="Cadastrar", command=self.cadastrar_usuario, style='TButton')
        btn_cadastrar.grid(row=6, column=0, pady=(15, 0), padx=10, ipady=8, sticky="ew")

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        login = self.entry_login.get()
        senha = self.entry_senha.get()

        if nome and login and senha:
            usuario = Usuario()

            # Autocompletar o código do usuário se baseando na última linha do arquivo usuario.txt
            with open('txt/usuarios.txt', 'r') as arquivo_usuarios:
                linhas = arquivo_usuarios.readlines()
                if linhas:
                    ultimo_codigo = int(linhas[-1].split(',')[0])
                    codigo_usuario = ultimo_codigo + 1
                else:
                    codigo_usuario = 1

            usuario.instanciar_usr(codigo_usuario, nome, "Cliente")

            # Verificação se o login já existe no arquivo
            with open('txt/usuarios.txt', 'r') as arquivo_usuarios:
                for linha in arquivo_usuarios:
                    dados = linha.strip().split(',')
                    if len(dados) >= 4 and dados[3] == login:
                        messagebox.showerror("Erro no Cadastro", "Login já existe. Escolha outro.")
                        return

            # Se o login não existir, pode criar um novo usuário
            usuario.getUsuarios()[login] = {'codigo': codigo_usuario, 'nome': nome, 'tipo': 'Cliente', 'senha': senha}

            # ler todo o conteúdo existente do arquivo
            with open('txt/usuarios.txt', 'r') as arquivo_usuarios:
                conteudo_existente = arquivo_usuarios.read()

            # Adicionar a nova linha
            nova_linha = f"{codigo_usuario},{nome},Cliente,{login},{senha}\n"
            conteudo_atualizado = conteudo_existente + nova_linha

            # escrever todo o conteúdo de volta no arquivo
            with open('txt/usuarios.txt', 'w') as arquivo_usuarios:
                arquivo_usuarios.write(conteudo_atualizado)

            messagebox.showinfo("Cadastro realizado", "Usuário cadastrado com sucesso.")
            self.master.destroy()  # Fechar a janela de cadastro após o cadastro ser concluído
        else:
            messagebox.showerror("Erro no Cadastro", "Preencha todos os campos.")

