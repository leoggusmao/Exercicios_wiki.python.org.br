#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.\n
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)\n
#deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.\n
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
#Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Qual o peso dos peixes em kg? '))
excesso = peso - 50

if peso > 50:
    multa = excesso * 4
    print(f'A quantidade de quilos em excesso, além do limite de 50 kg, foi de {excesso:,.2f} kg.')
    print(f'A multa a ser paga é de R$ {multa:,.2f}')
else: 
    print('A quantidade está dentro do limite estipulado no regulamento estadual.')