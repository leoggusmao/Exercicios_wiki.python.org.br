#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

penultimo = 0
ultimo = 1

print(1,end=',')

for i in range(499):
    soma = penultimo + ultimo
    penultimo = ultimo
    ultimo = soma
    if ultimo < 500:
        print(f'{soma},',end='')