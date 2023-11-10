#Faça um programa que calcule o mostre a média aritmética de N notas.

qtd_notas = int(input("Informe quantas notas quer informar: "))
notas = []

for i in range(1,qtd_notas+1):
    nota = float(input(f'Qual a {i}º nota? '))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f'A média das notas é {media:,.2f}')    