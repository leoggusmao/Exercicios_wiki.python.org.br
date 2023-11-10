#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # a)o produto do dobro do primeiro com metade do segundo.
    # b)a soma do triplo do primeiro com o terceiro.
    # c)o terceiro elevado ao cubo.

numero1 = int(input('Informe um número inteiro: '))
numero2 = int(input('Informe outro número inteiro: '))
numero3 = float(input('Informe um número real: '))
a = (2 * numero1) * (numero2 / 2)
b = 3 * numero1 + numero3
c = numero3 ** 3
print(f'o produto do dobro do primeiro com metade do segundo é {a:,.0f}')
print(f'a soma do triplo do primeiro com o terceiro é {b:,.2f}')
print(f'o terceiro elevado ao cubo é {c:,.2f}')