class Fornecedores:
    def __init__(self):
        self.__nomeFornecedor = ""
        self.__nomeProduto = ""
        self.__descricaoProduto = ""

    @property
    def _nomeFornecedor(self):
        return self.__nomeFornecedor

    @_nomeFornecedor.setter
    def _nomeFornecedor(self, value):
        self.__nomeFornecedor = value

    @property
    def _nomeProduto(self):
        return self.__nomeProduto

    @_nomeProduto.setter
    def _nomeProduto(self, value):
        self.__nomeProduto = value

    @property
    def _descricaoProduto(self):
        return self.__descricaoProduto

    @_descricaoProduto.setter
    def _descricaoProduto(self, value):
        self.__descricaoProduto = value

    def cadastrarFornecedor(self):
        self.__nomeFornecedor = input("Digite o nome do fornecedor: ")
        self.__nomeProduto = input("Digite o nome do produto: ")
        self.__descricaoProduto = input("Descreva o produto: ")

    def listarFornecedor(self):
        print ("\nNome do fornecedor: ", self.__nomeFornecedor)
        print ("Nome do produto: ", self.__nomeProduto)
        print("Descrição do produto: ", self.__descricaoProduto)