lista = ['Maria', 'Joao', 'Paulo', 'Magali']
buscar = 'Maria'
for i in lista:
    if i == buscar:
        print(f"Nome encontrado: {buscar}")
        break
    else:
        print("Nome não encontrado")