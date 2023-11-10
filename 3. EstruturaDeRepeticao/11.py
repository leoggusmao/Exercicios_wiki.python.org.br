#Altere o programa anterior para mostrar no final a soma dos números.

numero_1 = int(input("Informe o primeiro número: "))
numero_2 = int(input("Informe um segundo número maior que o primeiro: "))
soma = 0

for i in range(numero_1+1,numero_2):
    print(i,end=' ')
    soma += i

print(f'A soma é: {soma}')