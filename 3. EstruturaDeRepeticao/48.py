#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
#Exemplo:
#12376489
#=> 98467321

numero = int(input('Informe um número inteiro positivo: '))

print(numero)

numero_invertido = int(str(numero)[::-1])

print(numero_invertido)