def calcular_salario(valor_hora, qtd_hora):
    salario_bruto = valor_hora * qtd_hora
    desconto_ir = 0

    if salario_bruto > 900:
        ir_tabela = [1500, 2500]
        ir_aliquota = [0.05, 0.10]
        for i, limite in enumerate(ir_tabela):
            if salario_bruto <= limite:
                desconto_ir = salario_bruto * ir_aliquota[i]
                break
        else:
            desconto_ir = salario_bruto * 0.20

    inss = salario_bruto * 0.10
    fgts = salario_bruto * 0.11
    total_descontos = desconto_ir + inss

    return salario_bruto, desconto_ir, inss, fgts, total_descontos, salario_bruto - total_descontos


while True:
    valor_hora = float(input('Qual o valor da hora trabalhada? '))
    qtd_hora = int(input('Quantas horas foram trabalhadas no mês? '))

    salario_bruto, desconto_ir, inss, fgts, total_descontos, salario_liquido = calcular_salario(valor_hora, qtd_hora)

    print(f'Salário Bruto: ({valor_hora:.0f} * {qtd_hora})                         : R$ {salario_bruto:,.2f}\n'
          f'(-) IR ({desconto_ir*100/salario_bruto:.0f}%){" "*(42-len(str(desconto_ir*100/salario_bruto)))}: R$ {desconto_ir:,.2f}\n'
          f'(-) INSS (10%)                                    : R$ {inss:,.2f}\n'
          f'FGTS   (11%)                                      : R$ {fgts:,.2f}\n'
          f'Total de descontos                                : R$ {total_descontos:,.2f}\n'
          f'Salário Líquido                                   : R$ {salario_liquido:,.2f}')

    continuar = input("Deseja calcular o salário de outra pessoa? (s/n): ")
    if continuar.lower() != "s":
        break
