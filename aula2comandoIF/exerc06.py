import os
os.system('cls')

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

print("1 - média ponderada \n2 - quadrado da soma dos 2 números \n3 - cubo do menor número")
escolha=int(input("Escolha uma das opçoes acima: "))

if escolha==1:
    media=(num1*2+num2*3)/5
    print(f"média ponderada: {media}")
elif escolha==2:
    soma=num1+num2
    quadrado=pow(soma,2)
    print(f"Quadrado da soma dos 2 números: {quadrado}")
elif escolha==3:
    if num1<num2:
        cubo=pow(num1,3)
        print(f"Cubo do menor número: {cubo}")
    elif num2<num1:
        cubo=pow(num2,3)
        print(f"Cubo do menor número: {cubo}")
else:
    print("Opção inválida")
    exit()