#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)\n
#e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).\n
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    #Desconto do IR:
    #Salário Bruto até 900 (inclusive) - isento
    #Salário Bruto até 1500 (inclusive) - desconto de 5%
    #Salário Bruto até 2500 (inclusive) - desconto de 10%
    #Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

valor_hora = float(input('Qual o valor da hora trabalhada? '))
qtd_hora = int(input('Quantas horas foram trabalhadas no mês? '))
salario_bruto = valor_hora * qtd_hora

if salario_bruto <= 900:
        print(f'Salário Bruto: ({valor_hora:,.0f} * {qtd_hora})                       : R$ {salario_bruto:,.2f}\n'
          f'(-) IR (ISENTO)                                : R$ {salario_bruto * 0:,.2f}\n'
          f'(-) INSS (10%)                                 : R$ {salario_bruto * 0.10:,.2f}\n'
          f'FGTS   (11%)                                   : R$ {salario_bruto * 0.11:,.2f}\n'
          f'Total de descontos                             : R$ {salario_bruto * 0.10:,.2f}\n'
          f'Salário Líquido                                : R$ {salario_bruto - salario_bruto* 0.10:,.2f}') 
elif salario_bruto > 900 and salario_bruto <= 1500:
        print(f'Salário Bruto: ({valor_hora:,.0f} * {qtd_hora})                      : R$ {salario_bruto:,.2f}\n'
          f'(-) IR (5%)                                    : R$ {salario_bruto * 0.05:,.2f}\n'
          f'(-) INSS (10%)                                 : R$ {salario_bruto * 0.10:,.2f}\n'
          f'FGTS   (11%)                                   : R$ {salario_bruto * 0.11:,.2f}\n'
          f'Total de descontos                             : R$ {salario_bruto * 0.15:,.2f}\n'
          f'Salário Líquido                                : R$ {salario_bruto - salario_bruto* 0.15:,.2f}')
elif salario_bruto > 1500 and salario_bruto <= 2500:
        print(f'Salário Bruto: ({valor_hora:,.0f} * {qtd_hora})                      : R$ {salario_bruto:,.2f}\n'
          f'(-) IR (10%)                                   : R$ {salario_bruto * 0.10:,.2f}\n'
          f'(-) INSS (10%)                                 : R$ {salario_bruto * 0.10:,.2f}\n'
          f'FGTS   (11%)                                   : R$ {salario_bruto * 0.11:,.2f}\n'
          f'Total de descontos                             : R$ {salario_bruto * 0.20:,.2f}\n'
          f'Salário Líquido                                : R$ {salario_bruto - salario_bruto* 0.20:,.2f}')
elif salario_bruto > 2500:
        print(f'Salário Bruto: ({valor_hora:,.0f} * {qtd_hora})                       : R$ {salario_bruto:,.2f}\n'
          f'(-) IR (20%)                                    : R$ {salario_bruto * 0.20:,.2f}\n'
          f'(-) INSS (10%)                                  : R$ {salario_bruto * 0.10:,.2f}\n'
          f'FGTS   (11%)                                    : R$ {salario_bruto * 0.11:,.2f}\n'
          f'Total de descontos                              : R$ {salario_bruto * 0.30:,.2f}\n'
          f'Salário Líquido                                 : R$ {salario_bruto - salario_bruto* 0.30:,.2f}')        
