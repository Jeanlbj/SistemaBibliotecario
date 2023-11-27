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
                # .strip e .split para formatação ideal da linha do .txt
                codigo, cliente, livro, data = linha.strip().split(',')
                emprestimo = cls(codigo, cliente, livro, data)  # criando uma instancia da classe empréstimo
                emprestimos.append(emprestimo)
        return emprestimos

    @classmethod
    def listar_emprestimos(cls):
        emprestimos = cls.ler_emprestimos_do_arquivo()  # chama o método de ler empréstimos
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

    @classmethod
    def salvar_emprestimos_no_arquivo(cls, emprestimos):
        with open('txt/emprestimos.txt', 'w') as arquivo_emprestimos:
            for emprestimo in emprestimos:
                linha = f"{emprestimo.codigo},{emprestimo.cliente},{emprestimo.livro},{emprestimo.data}\n"
                arquivo_emprestimos.write(linha)
