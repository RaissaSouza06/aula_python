nomes = []
for i in range (1,8):
    n = str(input(f"Digite o {i}º nome:  "))
    nomes.append(n)

print("Nomes digitados: ")
c = 1
for i in nomes :
    print(f"O {c}º nome armazenado é: {i}")
    c +=1
