#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    # a)Para homens: (72.7*h) - 58
    # b)Para mulheres: (62.1*h) - 44.7

h = float(input('Qual a altura da pessoa? '))
sexo = input('Digite "h" para homem ou "m" para mulher ')

if sexo == "h":
    peso_ideal = 72.7 * h - 58
elif sexo == "m":
    peso_ideal = 62.1 * h - 44.7

print(f'O peso ideal para esta pessoa é {peso_ideal:,.2f} kg.')