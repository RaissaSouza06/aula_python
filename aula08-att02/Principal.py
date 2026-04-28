from Passagem import CadastroPassagens

class Principal:
    @staticmethod
    def main():
        cpa = CadastroPassagens()
        cpa.executar()

if __name__ == "__main__":
    Principal.main()