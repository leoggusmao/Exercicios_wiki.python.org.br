#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input('Qual o raio do círculo? '))
area = 3.1415926 * raio ** 2
print(f'A área do círculo é {area:,.2f}')