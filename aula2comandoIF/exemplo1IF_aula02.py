#exemplo estrutura condicional IF - media

nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2

#comando IF(se), ELIF(senão se) e ELSE(senão)
if media > 6.0:
    print(f"aluno aprovado, a média é: {media:.2f}")
elif media > 5.0 and media <6.0:
     print(f"aluno esta de exame, a média é: {media:.2f}")   
else:
    print(f"aluno reprovado, a média é: {media:.2f}")
