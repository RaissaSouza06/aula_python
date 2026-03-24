from Cadastro import Cadastro

class Principal:
    @staticmethod
    def main ():
        #instanciar classe a plicação
        apl = Cadastro()
        apl.executar()

if __name__ == "__main__":
    Principal.main()
