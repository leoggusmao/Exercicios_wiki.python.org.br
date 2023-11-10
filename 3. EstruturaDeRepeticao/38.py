#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
#Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

import datetime

salario_95 = float(input("Informe o salário inicial do funcionário em 1995: "))
aumento = 0.015
salario_96 = salario_95 * (1 + aumento)
salario_atual = salario_96
ano_atual = datetime.datetime.now().year

for ano in range(1996, ano_atual + 1):
    aumento *= 2

salario_atual = salario_96 * aumento

print(f'O salário atual em {ano_atual} é R$ {salario_atual:,.2f}')