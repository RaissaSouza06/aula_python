#comando para limpar a tela nas execução
import os 
os.system('cls')

num = int(input("Digite um número positivo: "))

if num%2==0:
    quadrado=pow(num,2)
    print(f"{num} elevado ao quadrado é: {quadrado}")
else:
    cubo=pow(num,3)
    print(f"{num} elevado ao cubo é: {cubo}")
