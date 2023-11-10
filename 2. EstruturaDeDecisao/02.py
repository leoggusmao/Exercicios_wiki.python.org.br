#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input('Informe um número positivo ou negativo: '))

if numero > 0:
    print(f'O número ({numero}) é positivo')
else:
    print(f'O número ({numero}) é negativo')