#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

numeros = []
intervalos = [[], [], [], []]

while True:
    numero = int(input("Informe um número positivo (ou um número negativo para encerrar): "))
    if numero < 0:
        break

    numeros.append(numero)

    if 0 <= numero <= 25:
        intervalos[0].append(numero)
    elif 26 <= numero <= 50:
        intervalos[1].append(numero)
    elif 51 <= numero <= 75:
        intervalos[2].append(numero)
    elif 76 <= numero <= 100:
        intervalos[3].append(numero)

print(f'A quantidade de números nos intervalos de [0-25]: {len(intervalos[0])}')
print(f'A quantidade de números nos intervalos de [26-50]: {len(intervalos[1])}')
print(f'A quantidade de números nos intervalos de [51-75]: {len(intervalos[2])}')
print(f'A quantidade de números nos intervalos de [76-100]: {len(intervalos[3])}')