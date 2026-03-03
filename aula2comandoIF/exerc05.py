import os
os.system('cls')

alt1=float(input("Digite a primeira altura: "))
alt2=float(input("Digite a segunda altura: "))
alt3=float(input("Digite a terceira altura: "))

if alt1>alt2 and alt1>alt3:
    maior = alt1
    if alt2>alt3:
        mediana = alt2
        menor = alt3
        print(f"maior altura: {maior} \naltura mediana: {mediana} \nmenor altura: {menor}")
    elif alt3>alt2:
        mediana = alt3
        menor = alt2
        print(f"maior altura: {maior} \naltura mediana: {mediana} \nmenor altura: {menor}")

if alt2>alt1 and alt2>alt3:
    maior = alt2
    if alt1>alt3:
        mediana = alt1
        menor = alt3
        print(f"maior altura: {maior} \naltura mediana: {mediana} \nmenor altura: {menor}")
    elif alt3>alt1:
        mediana = alt3
        menor = alt1
        print(f"maior altura: {maior} \naltura mediana: {mediana} \nmenor altura: {menor}")

if alt3>alt1 and alt3>alt2:
    maior = alt3
    if alt1>alt2:
        mediana = alt1
        menor = alt2
        print(f"maior altura: {maior} \naltura mediana: {mediana} \nmenor altura: {menor}")
    elif alt2>alt1:
        mediana = alt2
        menor = alt1
        print(f"maior altura: {maior} \naltura mediana: {mediana} \nmenor altura: {menor}")
