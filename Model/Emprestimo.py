class Emprestimo:
    def __init__(self, codigo, cliente, livro, data):
        self.codigo = codigo
        self.cliente = cliente
        self.livro = livro
        self.data = data

    @classmethod
    def ler_emprestimos_do_arquivo(cls):
        emprestimos = []
        with open('txt/emprestimos.txt', 'r') as arquivo_emprestimos:
            for linha in arquivo_emprestimos:
                codigo, cliente, livro, data = linha.strip().split(',')
                emprestimo = cls(codigo, cliente, livro, data)  # Cria uma instância da classe Emprestimo
                emprestimos.append(emprestimo)
        return emprestimos

    @classmethod
    def listar_emprestimos(cls):
        emprestimos = cls.ler_emprestimos_do_arquivo()  # Chama o método para ler os empréstimos
        if len(emprestimos) == 0:
            print("Não há empréstimos registrados.")
        else:
            print("### Lista de Empréstimos ###")
            for emprestimo in emprestimos:
                print(
                    f"Código: {emprestimo.codigo}, Cliente: {emprestimo.cliente}, "
                    f"Livro: {emprestimo.livro}, Data: {emprestimo.data}")

    @classmethod
    def adicionar_emprestimo(cls, emprestimo):
        with open('txt/emprestimos.txt', 'a') as arquivo_emprestimos:
            linha = f"{emprestimo.codigo},{emprestimo.cliente},{emprestimo.livro},{emprestimo.data}\n"
            arquivo_emprestimos.write(linha)