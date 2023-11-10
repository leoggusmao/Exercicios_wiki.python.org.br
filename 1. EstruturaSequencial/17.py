#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.\n
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,\n
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    #comprar apenas latas de 18 litros;
    #comprar apenas galões de 3,6 litros;
    #misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import remainder, ceil

area = float(input('Qual o tamanho em metros quadrados (m²) da área a ser pintada? '))
qtd_litros = area / 6
qtd_latas1 = ceil(qtd_litros / 18)
qtd_galoes1 = ceil(qtd_litros / 3.6)
resto = remainder((qtd_litros * 1.1), 18)
preco_lata = 80
preco_galao = 25

if resto < 18 and resto >= 0:
    qtd_latas2 = ceil((qtd_litros * 1.1 / 18))
    qtd_galoes2 = ceil(resto / 3.6)
else:
    qtd_latas2 = ceil((qtd_litros * 1.1 / 18))
    qtd_galoes2 = 0

print(f'1º situação: A quantidade de latas a serem compradas é {qtd_latas1:,.0f} e o preço total é de R$ {qtd_latas1 * preco_lata:,.2f}')
print(f'2º situação: A quantidade de galões a serem comprados é {qtd_galoes1:,.0f} e o preço total é de R$ {qtd_galoes1 * preco_galao:,.2f}')
print(f'3º situação: A quantidade de latas e galões a serem compradas é de {qtd_latas2:,.0f} e {qtd_galoes2:,.0f} respectivamente, e o preço total é de R$ {(qtd_latas2 * preco_lata) + (qtd_galoes2 * preco_galao):,.2f}')