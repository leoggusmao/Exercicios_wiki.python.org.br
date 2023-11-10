#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input('Qual o preço do 1º produto? '))
preco2 = float(input('Qual o preço do 2º produto? '))
preco3 = float(input('Qual o preço do 3º produto? '))

if preco1 < preco2 and preco1 < preco3:
    print('Compre o primeiro produto!')
elif preco2 < preco1 and preco2 < preco3:
    print('Compre o segundo produto!')
elif preco3 < preco1 and preco3 < preco2:
    print('Compre o terceiro produto!')