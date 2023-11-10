#Faça um programa que mostre os n termos da Série a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
#Imprima no final a soma da série.

n = int(input('Informe um número inteiro positivo: '))
soma = 0

for i in range(1,n+1):
    termo = i / (2 * i -1)
    soma += termo
    print(f'{i}/{2*i-1}', end=" + ")

print(f'\n\nSoma da série: {soma:,.2f}\n')