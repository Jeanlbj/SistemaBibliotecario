class Usuario:
    def __init__(self):
        self.__codigo = None
        self.__nome = None
        self.__tipo = None
        self.__login = None
        self.__senha = None
        self.__usuarios = {}

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_tipo(self):
        return self.__tipo

    def get_login(self):
        return self.__login

    def get_senha(self):
        return self.__senha

    def set_login(self, login):
        self.__login = login

    def set_senha(self, senha):
        self.__senha = senha

    def getUsuarios(self):
        return self.__usuarios

    def instanciar_usr(self, codigo, nome, tipo):
        self.__codigo = codigo
        self.__nome = nome
        self.__tipo = tipo

    def validar_acesso(self):
        # Lê o arquivo de usuários e armazena as informações em um dicionário
        with open('txt/usuarios.txt', 'r') as arquivo_usuarios:
            for linha in arquivo_usuarios:
                codigo, nome, tipo, login, senha = linha.strip().split(',')
                self.__usuarios[login] = {'codigo': codigo, 'nome': nome, 'tipo': tipo, 'senha': senha}
                if self.__login == login and self.__senha == senha:
                    codigo = self.__usuarios[login]['codigo']
                    nome = self.__usuarios[login]['nome']
                    tipo = self.__usuarios[login]['tipo']
                    self.instanciar_usr(codigo, nome, tipo)
                    return True
        return False

