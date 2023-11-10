#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Qual o valor da hora trabalhada? '))
qtd_hora = float(input('Quantas horas foram trabalhadas no mês? '))
salario_mes = valor_hora * qtd_hora
print(f'O seu salário no mês foi de R$ {salario_mes:,.2f}')