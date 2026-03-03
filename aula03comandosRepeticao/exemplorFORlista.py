# exemplo de for usando lista de valores pré definidos 
frutas =['banana', 'goiaba', 'abacaxi', 'abacate']
for lista in frutas:
    print(lista)

buscar = 'abacaxi'
frutas =['banana', 'goiaba', 'abacaxi', 'abacate']
# verifica cada variavel de frutas até achar o valor abacaxi da variavel buscar
for i in frutas:
    if i == buscar:
        print(f"fruta encontrada: {buscar}")
        break
    else:
        print(f"Fruta não encontrada: {buscar}")