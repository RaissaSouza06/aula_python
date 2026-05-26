# exemplo utilizando comando if
qtd = int(input("Digite uma quantidade: "))
valor = float(input("Digite um preço do produto: "))

if qtd > 10:
    valorTotal = (valor * qtd) - 10
    print(f"O desconto é de R$10, o valor a pagar é {valorTotal}")
elif qtd==10:
    valorTotal = valor * qtd
    print(f"Não há desconto, o valor a pagar é {valorTotal}")
else:
    valorTotal = (valor * qtd) - 5
    print(f"O desconto é de R$5, o valor a pagar é {valorTotal}")