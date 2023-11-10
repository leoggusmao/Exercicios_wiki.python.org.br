#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

qtd = int(input("Qual a quantidade de números usará? "))
lista = []

for i in range(qtd):
    while True: 
        numero = int(input(f'Qual o {i + 1}º número (entre 0 e 1000)? '))   
        if 0 < numero < 1000:
            lista.append(numero)
            break
        else:
            print('O número tem que estar entre 0 e 1000')            


menor = min(lista)
maior = max(lista)
soma = sum(lista)

print(f'O menor valor é {menor}, o maior é {maior} e a soma é {soma}')