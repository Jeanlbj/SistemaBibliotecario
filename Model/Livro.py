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
                livro = cls(codigo, titulo, autor)  # Cria uma instância da classe Livro
                livros.append(livro)
        return livros

    @classmethod
    def listar_livros(cls):
        livros = cls.ler_livros_do_arquivo()  # Chama o método para ler os livros
        if len(livros) == 0:
            print("Não há livros disponíveis.")
        else:
            print("### Lista de Livros ###")
            for livro in livros:
                print(f"Código: {livro.codigo}, Título: {livro.titulo}, Autor: {livro.autor}")
