#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro 

#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

gasolina = 2.50
alcool = 1.90

combustivel = input("Qual combústivel deseja abastecer? A - álcool    G - gasolina ").upper()
litros = float(input("Quantos litros deseja abastecer? "))

if combustivel == "A" and litros <= 20:
    valor = alcool * 0.97 * litros
elif combustivel == "A" and litros > 20:
    valor = alcool * 0.95 * litros
elif combustivel == "G" and litros <= 20:
    valor = gasolina * 0.96 * litros
elif combustivel == "G" and litros > 20:
    valor = gasolina * 0.94 * litros

print(f'O valor a ser pago é: R$ {valor:,.2f}')