from Contato import Contato

class Principal:
    @staticmethod
    def main ():
        #instanciar classe a plicação
        apl = Contato()
        apl.executar()

if __name__ == "__main__":
    Principal.main()
