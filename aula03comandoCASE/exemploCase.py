opc = int(input("1 - sacar \n2 - extrato \n3 - sair \nEscolha a opção2: "))

match opc:
    case 1:
        print("Você escolheu a opção sacar")
        valor = float(input("Digite o valor do saque: "))
        print(f"Sacando da sua conta ... o valor de R$ {valor}")
    case 2:
        print("Você escolheu a opção extrato")
        dias = int(input("Digite a quantidade de dias: "))
        print(f"Retirando extrato de {dias} dias...")
    case 3:
        exit
    case _:
        print("Opção inválida")
    