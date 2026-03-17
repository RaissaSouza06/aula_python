class Passagem:
    def __init__(self):
        self.__nomePassageiro = ""
        self.__telefone = ""
        self.__RG = ""
        self.__localViagem = ""
        self.__data = ""
        self.__horario = ""
        self.__numpoltrona = 0



    @property
    def _nomePassageiro(self):
        return self.__nomePassageiro

    @_nomePassageiro.setter
    def _nomePassageiro(self, value):
        self.__nomePassageiro = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

    @property
    def _RG(self):
        return self.__RG

    @_RG.setter
    def _RG(self, value):
        self.__RG = value

    @property
    def _localViagem(self):
        return self.__localViagem

    @_localViagem.setter
    def _localViagem(self, value):
        self.__localViagem = value

    @property
    def _data(self):
        return self.__data

    @_data.setter
    def _data(self, value):
        self.__data = value

    @property
    def _horario(self):
        return self.__horario

    @_horario.setter
    def _horario(self, value):
        self.__horario = value

    @property
    def _numpoltrona(self):
        return self.__numpoltrona

    @_numpoltrona.setter
    def _numpoltrona(self, value):
        self.__numpoltrona = value

    def cadastrarDadosPassageiro(self):
        self.__nomePassageiro = input("Digite o nome do passageiro: ")
        self.__telefone = input("Digite o número de telefone: ")
        self.__RG = input("Digite o RG: ")

    def cadastrarDadosPassagem(self):
        self.__localViagem = input("Digite o nome do local de viagem: ")
        self.__data = input("Digite a data: ")
        self.__horario = input("Digite o horário: ")
        self.__numpoltrona = input("Digite o número da poltrona: ")

    def mostrarDadosPassageiro(self):
        print("\nNome do passageiro: ", self.__nomePassageiro)
        print("Telefone do passageiro: ", self.__telefone)
        print("RG do passageiro: ", self.__RG)

    def mostrarDadosPassagem(self):
        print("Local de viagem: ", self.__localViagem)
        print("Data da viagem: ", self.__data)
        print("Horário da viagem: ", self.__horario)
        print("Número da poltrona: ", self.__numpoltrona)