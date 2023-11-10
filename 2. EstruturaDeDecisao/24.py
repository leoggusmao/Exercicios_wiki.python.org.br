#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

numero1 = float(input("Digite o 1º número: "))
numero2 = float(input("Digite o 2º número: "))

operacao = int(input("Qual operação deseja realizar? 1- Soma, 2- Subtração, 3- Multiplicação ou 4- Divisão "))
if operacao > 4 or operacao < 1:
    print ("Opção Inválida")
else:
    if operacao == 1:
        resultado = numero1 + numero2
    elif operacao == 2:
        resultado = numero1 - numero2
    elif operacao == 3:
        resultado = numero1 * numero2
    else:
        resultado = numero1 / numero2

if resultado % 2 == 0:
    var1 = "par"
else:
    var1 = "impar"

if resultado > 0:
    var2 = "positivo"
else:
    var2 = "negativo"

if resultado == round(resultado):
    var3 = "inteiro"
else:
    var3 = "decimal"

print(f'O resultado é {resultado}, {var1}, {var2}, {var3}')