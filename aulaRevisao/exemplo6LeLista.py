# armazena os valores em uma lista que foi digitada pelo usuário
pessoas = []

for lista in range(1,6):
    p = input(f"Digite o nome da {lista}ª pessoa")
    # armazenar dados no vetor
    pessoas.append(p)

# mostrar os nomes
for i in pessoas:
    print(i)