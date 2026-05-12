from Oficina import CadastroMecanica

class Principal:
    @staticmethod
    def main():
        cpo = CadastroMecanica()
        cpo.executar()

if __name__ == "__main__":
    Principal.main()