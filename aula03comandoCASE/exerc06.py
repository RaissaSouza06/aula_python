peso_terra = float(input("Digite o seu peso na Terra (kg): "))

print("\nEscolha o planeta para saber seu peso lá:")
print("1 - Mercúrio")
print("2 - Vênus")
print("3 - Marte")
print("4 - Júpiter")
print("5 - Saturno")

opcao = int(input("\nDigite o número do planeta: "))

if opcao == 1:
    peso_planeta = peso_terra * 0.37
    print(f"Seu peso em Mercúrio é: {peso_planeta:.2f} kg")
elif opcao == 2:
    peso_planeta = peso_terra * 0.88
    print(f"Seu peso em Vênus é: {peso_planeta:.2f} kg")
elif opcao == 3:
    peso_planeta = peso_terra * 0.38
    print(f"Seu peso em Marte é: {peso_planeta:.2f} kg")
elif opcao == 4:
    peso_planeta = peso_terra * 2.64
    print(f"Seu peso em Júpiter é: {peso_planeta:.2f} kg")
elif opcao == 5:
    peso_planeta = peso_terra * 1.15
    print(f"Seu peso em Saturno é: {peso_planeta:.2f} kg")
else:
    print("Opção inválida. Digite um número de 1 a 5.")