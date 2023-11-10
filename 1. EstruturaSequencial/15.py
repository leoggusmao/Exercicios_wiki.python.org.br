#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.\n
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,\n
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    # a)salário bruto.
    # b)quanto pagou ao INSS.
    # c)quanto pagou ao sindicato.
    # d)o salário líquido.
    # e)calcule os descontos e o salário líquido, conforme a tabela abaixo:
        # + Salário Bruto : R$
        # - IR (11%) : R$
        # - INSS (8%) : R$
        # - Sindicato ( 5%) : R$
        # = Salário Liquido : R$
        # Obs.: Salário Bruto - Descontos = Salário Líquido

valor_hora = float(input('Qual o valor da hora trabalhada? '))
qtd_hora = float(input('Quantas horas foram trabalhadas no mês? '))
salario_bruto = valor_hora * qtd_hora
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print(f'O seu salário bruto no mês foi de R$ {salario_bruto:,.2f}\n'
      f'Pagou de INSS e sindicato o total de R$ {inss:,.2f} e R$ {sindicato:,.2f}, respectivamente\n'
      f'Ficou com um salário líquido de R$ {salario_liquido:,.2f}')