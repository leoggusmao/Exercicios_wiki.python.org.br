#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input("Informe um número inteiro para fatoração: "))
fatoracao = 1
etapas = ''

for i in range(1,numero+1):
    fatoracao *= i
    etapas += str(i)
    if i < numero:
        etapas += ' * '

print(f'{numero}! = {etapas} = {fatoracao}')