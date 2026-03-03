numeros = []
pares = []
impares = []

# Lendo 10 números
for i in range(1, 11):
    n = int(input(f"Digite o {i}º número: "))
    numeros.append(n)

# Verificando se são pares ou ímpares
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Mostrando os resultados
print("\nNúmeros pares:", pares)
print("Números ímpares:", impares)