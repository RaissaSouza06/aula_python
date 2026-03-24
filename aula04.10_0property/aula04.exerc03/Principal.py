from Loja import Loja

class Principal:
    @staticmethod
    def main():
        loja = Loja()
        loja.inserirDadosLoja()
        loja.calcularCompraLoja()
        print(loja.mostrarDadosLoja())

if __name__=="__main__":
    Principal.main()