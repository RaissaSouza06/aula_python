indice = int(input("Digite o valor do índice de poluição: "))

match indice:
    case 0 | 1 | 2:
        print("Segundo a Secretaria do Meio Ambiente é consideravel áceitavel")
    case 3 | 4 | 5:
        print("Segundo a Secretaria do Meio Ambiente é necessário suspender atividades do grupo I")
    case 6 | 7:
        print("Segundo a Secretaria do Meio Ambiente é necessário suspender atividades do grupo II")
    case _:
        print("Segundo a Secretaria do Meio Ambiente é necessário suspender atividades de todos os grupos")


