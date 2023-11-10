#Faça um programa que leia 5 números e informe a soma e a média dos números.

numero_1 = float(input("Informe o 1º número: "))
numero_2 = float(input("Informe o 2º número: "))
numero_3 = float(input("Informe o 3º número: "))
numero_4 = float(input("Informe o 4º número: "))
numero_5 = float(input("Informe o 5º número: "))

soma = numero_1 + numero_2 + numero_3 + numero_4 + numero_5
media = (numero_1 + numero_2 + numero_3 + numero_4 + numero_5) / 5

print(f'A soma dos núemros é {soma:,.2f}, e a média é {media:,.2f}')