from Fornecedores import Fornecedores

class Principal:
    @staticmethod
    def main():
        forn = Fornecedores()
        forn.cadastrarFornecedor()
        forn.listarFornecedor()
if __name__ == "__main__":
    Principal.main()