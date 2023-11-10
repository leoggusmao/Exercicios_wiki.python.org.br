#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura = float(input('Qual a temperatura em Celsius? '))
conversao = temperatura * 9 / 5 + 32
print(f'A temperatura em graus Fahrenheit é de {conversao:,.2f} °F')