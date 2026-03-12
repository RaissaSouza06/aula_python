class Produto:

    def __init__(self,nome,preco,qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    #método mostrar info dos produtos
    def mostrar(self):
        print("Nome produto: ", self.nome) # usa self pq ainda esta dentro da classe
        print("Preço produto: ", self.preco)
        print("Quantidade  produto: ", self.qtd)

    #método calcular valor total
    def calcularTotal(self):
        valor_total = self.qtd * self.preco
        print(f"O valor toal é R$ {valor_total}")

#instanciando os objetos e chamar os métodos das classes 
prod = Produto('abaca',4.5,3)
prod.mostrar()
prod.calcularTotal()
