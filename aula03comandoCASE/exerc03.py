print("****** CÁLCULO DE GRANDEZAS ELÉTRICAS ******")
opc = int(input("1 - Tensão \n2 - Resistência \n3 - Corrente \nEscolha uma opção: "))

match opc:
    case 1:
        r = int(input("Digite o valor da resistência: "))
        i = int(input("Digite o valor da corrente: "))
        tensão = r*i
        print(f"Valor da tensão = {tensão} Volt")
    case 2:
        i = int(input("Digite o valor da corrente: "))
        u = int(input("Digite o valor da tensão: "))
        resistencia = u/i
        print(f"Valor da resistencia = {resistencia} Ohm")
    case 3:
        u = int(input("Digite o valor da tensão: "))
        r = int(input("Digite o valor da resistência: "))
        corrente = u/r
        print(f"Valor da corrente = {corrente} Ampere")



