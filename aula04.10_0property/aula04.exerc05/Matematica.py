class Matematica:
    def __init__(self):
        self.__nota1 = 0.0
        self.__nota2 = 0.0
        self.__media = 0.0
        self.__nomeAluno = ""

    @property
    def _nota1(self):
        return self.__nota1

    @_nota1.setter
    def _nota1(self, value):
        self.__nota1 = value

    @property
    def _nota2(self):
        return self.__nota2

    @_nota2.setter
    def _nota2(self, value):
        self.__nota2 = value

    @property
    def _media(self):
        return self.__media

    @_media.setter
    def _media(self, value):
        self.__media = value

    @property
    def _nomeAluno(self):
        return self.__nomeAluno

    @_nomeAluno.setter
    def _nomeAluno(self, value):
        self.__nomeAluno = value

    def inserirNotas(self):
        self.__nomeAluno = input("Digite o nome do aluno: ")
        self.__nota1 = float(input("Digite a primeira nota: "))
        self.__nota2 = float(input("Digite a segunda nota: "))

    def calcularMedia(self):
        self.__media = (self.__nota1 + self.__nota2) / 2
        return (self.__media)
    
    def mostrarNomeMedia(self):
        return("\n--- exibindo nome e média ---\n"
               f"Nome do aluno: {self.__nomeAluno}\n"
               f"Média do aluno: {self.__media:.2f}")