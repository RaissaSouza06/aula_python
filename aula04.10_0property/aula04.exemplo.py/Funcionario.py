class Funcionario:
    def __init__(self):
        self.__nome =  ""
        self.__idade = 0
        self.__salarioAtual = 0.0
        self.__salAumento = 0.0

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _idade(self):
        return self.__idade

    @_idade.setter
    def _idade(self, value):
        self.__idade = value

    @property
    def _salarioAtual(self):
        return self.__salarioAtual

    @_salarioAtual.setter
    def _salarioAtual(self, value):
        self.__salarioAtual = value

    @property
    def _salAumento(self):
        return self.__salAumento

    @_salAumento.setter
    def _salAumento(self, value):
        self.__salAumento = value

# função cadastrar funcionario
    def cadastrarFunc(self):
        self.__nome = input("Digite o nome do funcionário: ")
        self.__idade = int(input("Digite a idade: "))
        self.__salarioAtual = float(input("Digite salário atual: "))

    def calcularAumento(self):
        self.__salAumento = self.__salarioAtual + (self.__salarioAtual * 10)/100
        return self.__salAumento

