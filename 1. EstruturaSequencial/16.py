#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.\n
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.\n
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

area = float(input('Qual o tamanho em metros quadrados (m²) da área a ser pintada? '))
qtd_latas = math.ceil(area / 3 / 18)
preco_total = qtd_latas * 80
print(f'A quantidade de latas a serem compradas é {qtd_latas:,.0f} e o preço total é de R$ {preco_total:,.2f}')