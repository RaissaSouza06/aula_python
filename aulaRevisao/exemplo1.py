op = int(input("Digite a opção: \n1-Calculo Perimetro \n2-Calculo area \n3-Sair"))

match op:
    case 1:
        # exemplo de leitura de dados e conversão de valores
        ladoa = float(input("Digite o lado A do retangulo: "))
        ladob = float(input("Digite o lado B do retangulo: "))

        calculo = 2*ladoa + 2*ladob

        # para converter o resultado com dois numeros após a vírgula -> :.2f
        print(f"O resultado do perimetro do é {calculo:.2f}")

    case 2:
        # exemplo de leitura de dados e conversão de valores
        ladoa = float(input("Digite o lado A do retangulo: "))
        ladob = float(input("Digite o lado B do retangulo: "))

        calculo = ladoa*ladob

        # para converter o resultado com dois numeros após a vírgula -> :.2f
        print(f"O resultado da area do é {calculo:.2f}")
    
    case 3:
        exit #sai da aplicação
    
    case _:
        print("Opção incorreta")