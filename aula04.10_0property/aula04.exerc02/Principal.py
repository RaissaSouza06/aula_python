from Passagem import Passagem

class Principal:
    @staticmethod
    def main():
        passagem = Passagem()
        passagem.cadastrarDadosPassageiro()
        passagem.cadastrarDadosPassagem()
        passagem.mostrarDadosPassageiro()
        passagem.mostrarDadosPassagem()

if __name__ == "__main__":
    Principal.main()