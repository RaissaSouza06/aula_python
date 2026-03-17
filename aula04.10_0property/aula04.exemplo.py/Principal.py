from Funcionario import Funcionario

class Principal:
    @staticmethod
    def main():
        func = Funcionario() #instanciando o objeto funcionario

        func.cadastrarFunc()
        print("O aumento é R$ ", func.calcularAumento())

if __name__ == "__main__":
    Principal.main()