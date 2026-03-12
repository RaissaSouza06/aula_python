class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome,
        self.idade = idade

    #método calcular idade
    def calcularIdade(self):
        anoatual = int(input("Digite o ano atual: "))
        return anoatual - self.idade
    
#instanciar objeto da classe pessoa
p = Pessoa('Luiz', 25)
pe = Pessoa ('Joao', 56)
print(p.calcularIdade())
print(pe.calcularIdade())
print(f"Voce {pe.nome} nasceu em {pe.calcularIdade()}")