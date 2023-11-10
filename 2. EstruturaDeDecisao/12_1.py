# Loop principal para o cálculo do salário
while True:
    valor_hora = float(input('Qual o valor da hora trabalhada? '))
    qtd_hora = int(input('Quantas horas foram trabalhadas no mês? '))
    salario_bruto = valor_hora * qtd_hora

    if salario_bruto <= 900:
        print(f'Salário Bruto: ({valor_hora:,.0f} * {qtd_hora})                       : R$ {salario_bruto:,.2f}\n'
              f'(-) IR (ISENTO)                                : R$ {salario_bruto * 0:,.2f}\n'
              f'(-) INSS (10%)                                 : R$ {salario_bruto * 0.10:,.2f}\n'
              f'FGTS   (11%)                                   : R$ {salario_bruto * 0.11:,.2f}\n'
              f'Total de descontos                             : R$ {salario_bruto * 0.10:,.2f}\n'
              f'Salário Líquido                                : R$ {salario_bruto - salario_bruto * 0.10:,.2f}')
    elif salario_bruto > 900 and salario_bruto <= 1500:
        print(f'Salário Bruto: ({valor_hora:,.0f} * {qtd_hora})                      : R$ {salario_bruto:,.2f}\n'
              f'(-) IR (5%)                                    : R$ {salario_bruto * 0.05:,.2f}\n'
              f'(-) INSS (10%)                                 : R$ {salario_bruto * 0.10:,.2f}\n'
              f'FGTS   (11%)                                   : R$ {salario_bruto * 0.11:,.2f}\n'
              f'Total de descontos                             : R$ {salario_bruto * 0.15:,.2f}\n'
              f'Salário Líquido                                : R$ {salario_bruto - salario_bruto * 0.15:,.2f}')
    elif salario_bruto > 1500 and salario_bruto <= 2500:
        print(f'Salário Bruto: ({valor_hora:,.0f} * {qtd_hora})                      : R$ {salario_bruto:,.2f}\n'
              f'(-) IR (10%)                                   : R$ {salario_bruto * 0.10:,.2f}\n'
              f'(-) INSS (10%)                                 : R$ {salario_bruto * 0.10:,.2f}\n'
              f'FGTS   (11%)                                   : R$ {salario_bruto * 0.11:,.2f}\n'
              f'Total de descontos                             : R$ {salario_bruto * 0.20:,.2f}\n'
              f'Salário Líquido                                : R$ {salario_bruto - salario_bruto * 0.20:,.2f}')
    elif salario_bruto > 2500:
        print(f'Salário Bruto: ({valor_hora:,.0f} * {qtd_hora})                       : R$ {salario_bruto:,.2f}\n'
              f'(-) IR (20%)                                    : R$ {salario_bruto * 0.20:,.2f}\n'
              f'(-) INSS (10%)                                  : R$ {salario_bruto * 0.10:,.2f}\n'
              f'FGTS   (11%)                                    : R$ {salario_bruto * 0.11:,.2f}\n'
              f'Total de descontos                              : R$ {salario_bruto * 0.30:,.2f}\n'
              f'Salário Líquido                                 : R$ {salario_bruto - salario_bruto * 0.30:,.2f}')

    continuar = input("Deseja calcular o salário de outra pessoa? (s/n): ")
    if continuar.lower() != "s":
        break
