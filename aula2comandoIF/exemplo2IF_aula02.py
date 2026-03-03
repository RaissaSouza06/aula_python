#comando para limpar a tela nas execução
import os 
os.system('cls')

#estrutura if operadores relacionais: AND(e), OR(ou)
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1==num2 or num1==num3 or num2==num3:
    exit()  #termina a execução 
if num1>num2 and num1>num3:
    print("O primeiro numero é maior")
if num2>num1 and num2>num3:
    print("O segundo numero é maior")
if num3>num1 and num3>num2:
    print("O terceiro numero é maior")

