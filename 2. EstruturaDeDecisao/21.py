#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#   Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#   Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_saque = float(input("Qual valor deseja sacar? "))

qtd_100 = valor_saque // 100
resto = valor_saque % 100
qtd_50 = resto // 50
resto = resto % 50
qtd_10 = resto // 10
resto = resto % 10
qtd_5 = resto // 5
resto = resto % 5
qtd_1 = resto

print(f'{qtd_100:.0f} notas de 100, {qtd_50:.0f} notas de 50, {qtd_10:.0f} notas de 10, {qtd_5:.0f} notas de 5 e {qtd_1:.0f} notas de 1.')