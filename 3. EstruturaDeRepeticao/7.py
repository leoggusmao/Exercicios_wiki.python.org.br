#Faça um programa que leia 5 números e informe o maior número.

numero_1 = int(input("Informe o 1º número: "))
numero_2 = int(input("Informe o 2º número: "))
numero_3 = int(input("Informe o 3º número: "))
numero_4 = int(input("Informe o 4º número: "))
numero_5 = int(input("Informe o 5º número: "))

lista = [numero_1,numero_2,numero_3,numero_4,numero_5]
print("O maior número dos números é:",max(lista))