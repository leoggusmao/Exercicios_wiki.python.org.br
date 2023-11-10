#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

numero_1 = int(input("Informe o primeiro número: "))
numero_2 = int(input("Informe um segundo número maior que o primeiro: "))

for i in range(numero_1+1,numero_2):
    print(i,end=' ')