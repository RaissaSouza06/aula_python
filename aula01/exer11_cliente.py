descricao = str(input("Digite a descrição do produto: "))
qtd = int(input("Digite a quantidade de produto comprada: "))
preco = float(input("Digite o valor: "))

total = qtd*preco
print(f"Valor total a pagar: R${total}")
print(f"Descrição do produto: {descricao}")