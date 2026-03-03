nulo = int(input("Digite o número de votos nulos: "))
branco = int(input("Digite o número de votos brancos: "))
valido = int(input("Digite o número de votos válidos: "))

total = nulo+branco+valido
perbranco = (branco*100)/total
pernulo = (nulo*100)/total
pervalido = (valido*100)/total

print(f"Percentual de votos brancos: {perbranco:.2f}%")
print(f"Percentual de votos nulos: {pernulo:.2f}%")
print(f"Percentual de votos validos: {pervalido:2f}%")