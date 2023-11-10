#Faça um Programa que peça dois números e imprima o maior deles.

numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe mais um número: '))

if numero1 > numero2:
    print(f'O maior número é {numero1:,.2f}')
else:
    print(f'O maior número é {numero2:,.2f}')