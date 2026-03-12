# criar classe carro

class Carro:
    #construtor da classe
    def __init__(self,nome):
        self.nome = nome #self = meu construtor

    #método da classe carro
    def acelerar(self):
        print(self.nome , "Esta acelerando")

#instanciando objeto car da classe carro
car = Carro('Fusca')
print(car.nome)
car.acelerar()

c = Carro('Uno')
print(c.nome)
c.acelerar()