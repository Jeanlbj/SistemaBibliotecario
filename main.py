def validar_acesso():
    usuarios = {}

    # Lê o arquivo de usuários e armazena as informações em um dicionário
    with open('txt/usuarios.txt', 'r') as arquivo_usuarios:
        for linha in arquivo_usuarios:
            codigo, nome, tipo, login, senha = linha.strip().split(',')
            usuarios[login] = {'codigo': codigo, 'nome': nome, 'tipo': tipo, 'senha': senha}

    login = input("Login: ")
    senha = input("Senha: ")

    if login in usuarios and usuarios[login]['senha'] == senha:
        nome_do_usuario = usuarios[login]['nome']
        print(f"Bem-vindo(a), {nome_do_usuario}!")

    else:
        print("Acesso negado. Credenciais inválidas.")


if __name__ == '__main__':
    validar_acesso()
