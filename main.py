from Model.Usuario import Usuario


if __name__ == '__main__':
    usuario = Usuario()
    usuario.set_login(input("Login: "))
    usuario.set_senha(input("Senha: "))

    if usuario.validar_acesso():
        print(f"Acesso permitido! Bem vindo(a) {usuario.get_nome()}.")
    else:
        print("Acesso Negado!")
