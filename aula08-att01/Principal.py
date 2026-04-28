from Produto import CadastroProdutos

class Principal:
    @staticmethod
    def main():
        cpo = CadastroProdutos()
        cpo.executar()

if __name__ == "__main__":
    Principal.main()