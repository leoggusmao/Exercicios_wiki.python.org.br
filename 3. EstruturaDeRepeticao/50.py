#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = int(input('Informe um número inteiro positivo: '))
H = 0

for i in range(1,n+1):
    termo = 1 / i
    H += termo
    print(f'1/{i}', end=" + ")

print(f'\n\nH = {H:,.2f}\n')