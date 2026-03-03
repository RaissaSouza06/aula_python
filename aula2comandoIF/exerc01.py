#comando para limpar a tela nas execução
import os 
os.system('cls')

num1 = float(input("Digite o valor do primeiro número: "))
num2 = float(input("Digite o valor do segundo número: "))

if num1==num2:
    print("Os números são iguais")
elif num1>num2:
    media = num1/num2
    print(f"Valor da divisão: {media}")
else:
    media = num2/num1
    print(f"Valor da divisão: {media}")