#Faça um Programa que leia três números e mostre o maior deles.

numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))
numero3 = float(input('Informe o terceiro número: '))

if numero1 > numero2 and numero2 > numero3:
    print(f'O maior número é {numero1:,.0f}')
elif numero2 > numero1 and numero2 > numero3:
    print(f'O maior número é {numero2:,.0f}')
else:
    print(f'O maior número é {numero3:,.0f}')