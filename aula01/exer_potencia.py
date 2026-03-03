num = float(input("Digite o número: "))
exp = float(input("Digite o expoente: "))

#Potência utilizando operaador 
pot = num**exp

#Potênia usando a função math (função usada p várias operações matemáticas)
pote = pow(num,exp)
# se quero elevador ao quadrado - pote=pow(num,2)

print(f"O resultado da potência pot é: {pot}")
print(f"O resultado da potência pote é: {pote}")