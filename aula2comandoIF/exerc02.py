#comando para limpar a tela nas execução
import os 
os.system('cls')

nome1 = (input("Digite o primeiro nome: "))
peso1 = float(input("Digite o peso da primeira pessoa: "))
nome2 = (input("Digite o segundo nome: "))
peso2 = float(input("Digite o peso da segunda pessoa: "))

if peso1>peso2:
    print(f"O(a) {nome1} é mais pesado(a), seu peso é de {peso1}kg")
elif peso2>peso1:
        print(f"O(a) {nome2} é mais pesado(a), seu peso é de {peso2}kg")
else:
      print("Ambos possuem o mesmo peso")