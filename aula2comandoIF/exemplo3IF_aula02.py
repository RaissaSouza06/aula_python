#comando para limpar a tela nas execução
import os 
os.system('cls')

print('$$$ Programa de empréstimos $$$ \n Responda (0-não, 1-sim)')

#IF ANINHADO

negativo = int(input("Possui nome negativo? "))
if negativo == 1:
    print("Você não pode realizar empréstimos")
else:
    cartas = int(input("Você possui carteira assinada? "))
    if cartas == 0:
        print("Você não pode realizar empréstimos")
    else:
        casa = int(input("Você possui casa própria? "))
        if casa == 0:
            print("Não pode realizar empréstimo")
        else:
            print("Conceder o empréstimo")