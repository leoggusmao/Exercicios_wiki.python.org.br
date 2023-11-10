#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Informe a base da exponenciação: "))
expoente = int(input("Informe o expoente da operação: "))
resultado = base

for i in range(expoente-1):
    resultado *= base

print(f'O resultado é: {resultado}')