#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('Qual a primeira nota bimestral? '))
nota2 = float(input('Qual a segunda nota bimestral? '))
nota3 = float(input('Qual a terceira nota bimestral? '))
nota4 = float(input('Qual a quarta nota bimestral? '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média das notas é {media:.2f}')