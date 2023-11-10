#Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))
numero3 = float(input('Informe o terceiro número: '))

if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
    print(f'O maior número é {numero1:,.0f} e o menor é {numero3:,.0f}')
elif numero1 > numero2 and numero1 > numero3 and numero3 > numero2:
    print(f'O maior número é {numero1:,.0f} e o menor é {numero2:,.0f}')
elif numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
    print(f'O maior número é {numero2:,.0f} e o menor é {numero1:,.0f}')
elif numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
    print(f'O maior número é {numero2:,.0f} e o menor é {numero1:,.0f}')   
elif numero3 > numero1 and numero3 > numero2 and numero1 > numero2:
    print(f'O maior número é {numero3:,.0f} e o menor é {numero2:,.0f}')
else:
    print(f'O maior número é {numero3:,.0f} e o menor é {numero1:,.0f}')