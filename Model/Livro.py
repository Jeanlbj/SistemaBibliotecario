class Livro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor

    @classmethod
    def ler_livros_do_arquivo(cls):
        livros = []
        with open('txt/livros.txt', 'r') as arquivo_livros:
            for linha in arquivo_livros:
                codigo, titulo, autor = linha.strip().split(',')
                livro = cls(codigo, titulo, autor)  # criando uma instância da classe livro
                livros.append(livro)
        return livros

    @classmethod
    def listar_livros(cls):
        livros = cls.ler_livros_do_arquivo()  # chama o método para ler livros
        if len(livros) == 0:
            print("Não há livros disponíveis.")
        else:
            print("### Lista de Livros ###")
            for livro in livros:
                print(f"Código: {livro.codigo}, Título: {livro.titulo}, Autor: {livro.autor}")

    @classmethod
    def adicionar_livro(cls, livro):
        with open('txt/livros.txt', 'a') as arquivo_livros:
            linha = f"{livro.codigo},{livro.titulo},{livro.autor}\n"
            arquivo_livros.write(linha)

    @staticmethod
    def obter_proximo_codigo_livro():
        # lê o arquivo de livros e identifica o último código
        with open('txt/livros.txt', 'r') as arquivo_livros:
            linhas = arquivo_livros.readlines()
            if linhas:
                ultimo_codigo = int(linhas[-1].split(',')[0])
                proximo_codigo = ultimo_codigo + 1
            else:
                proximo_codigo = 1

        return proximo_codigo
