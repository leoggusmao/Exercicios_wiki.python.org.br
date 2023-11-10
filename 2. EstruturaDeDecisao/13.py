#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int((input('Digite um número: ')))

if numero == 1:
    print(f'{numero}- Domingo')
elif numero == 2:
    print(f'{numero}- Segunda')
elif numero == 3:
    print(f'{numero}- Terça')
elif numero == 4:
    print(f'{numero}- Quarta')
elif numero == 5:
    print(f'{numero}- Quinta')
elif numero == 6:
    print(f'{numero}- Sexta')
elif numero == 7:
    print(f'{numero}- Sábado')
else:
    print('Valor inválido.')