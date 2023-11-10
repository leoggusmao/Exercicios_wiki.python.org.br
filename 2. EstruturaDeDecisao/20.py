#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#   a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#   b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#   c) A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))
nota3 = float(input("Qual a terceira nota? "))
media = (nota1 + nota2 + nota3)/3

if media == 10:
    print(f"Aprovado com Distinção - média = {media:,.2f}")
elif media >= 7:
    print(f"Aprovado - média = {media:,.2f}")
else:
    print(f"Reprovado - média = {media:,.2f}")