#comando para limpar a tela nas execução
import os 
os.system('cls')

altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo: M-masculino, F-feminino ")

#função UPPER - transforma o q for em maiusculo em minusculo ou vice e versa

if sexo.upper() == "M":
    imc = (72.7*altura)-58
    print(f"Sua altura é {altura}m, seu sexo é masculino e seu peso ideal é {imc}kg")
elif sexo.upper() == "F":
    imc = (62.1*altura)-44.7
    print(f"Sua altura é {altura}m, seu sexo é feminino e seu peso ideal é {imc}kg")
else:
    print("Digite o sexo corretamente")