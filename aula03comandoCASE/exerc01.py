letra = str(input("Digite uma letra: "))

match letra.lower():
    case "a" | "e" | "i" | "o" | "u":
        print("Você digitou uma vogal") 
    case _:
        print("Você digitou uma consoante")