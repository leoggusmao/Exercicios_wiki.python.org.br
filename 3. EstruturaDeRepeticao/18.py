#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

qtd = int(input("Qual a quantidade de números usará? "))
lista = []

for i in range(qtd):
    numero = int(input(f'Qual o {i + 1}º número? '))
    lista.append(numero)

menor = min(lista)
maior = max(lista)
soma = sum(lista)

print(f'O menor valor é {menor}, o maior é {maior} e a soma é {soma}')