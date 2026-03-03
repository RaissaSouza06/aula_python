import os
os.system('cls')

rg=int(input("Digite seu RG: "))
nasc=int(input("Digite o ano do seu nascimento: "))
ingresso=int(input("Digite o seu ano de ingresso na empresa: "))
ano_atual=int(input("Digite o ano atual: "))

idade = ano_atual-nasc
tempotrabalho=ano_atual-ingresso

#print("Responda com '0' para não e com '1' para sim")
#idade=int(input("Possui no mínimo 65 anos?"))
#if idade==0:
#    print("Não ")

if idade>=65:
    print("requerer aposentadoria")
if tempotrabalho>=30:
    print("requerer aposentadoria")
if idade>=60 and  tempotrabalho>=25:
    print("requerer aposentadoria")
else:
    print("não requerer aposentadoria")