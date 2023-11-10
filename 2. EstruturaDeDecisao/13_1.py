#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
numero = int(input('Digite um número: '))

if 1 <= numero <= 7:
    print(f'{numero}- {dias_semana[numero-1]}')
else:
    print('Valor inválido.')