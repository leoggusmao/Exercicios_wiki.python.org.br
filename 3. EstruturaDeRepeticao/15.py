#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

limite = int(input('Informe o n-ésimo termo da sequência de Fibonacci: '))
penultimo = 0
ultimo = 1

print(1,end=',')

for i in range(limite-1):
    soma = penultimo + ultimo
    penultimo = ultimo
    ultimo = soma
    if i < limite - 1:
        print(f'{soma},',end='')
    elif i == limite -1:
        print(',...',end=' ')