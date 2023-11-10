#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#1       0
#3       10
#6       15
#9       20
#12      25
#Exemplo de saída do programa:
#Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#R$ 1.000,00     0               1                       R$  1.000,00
#R$ 1.100,00     100             3                       R$    366,00
#R$ 1.150,00     150             6                       R$    191,67

divida = float(input("Informe o valor da dívida: "))
parcelas = [1, 3, 6, 9, 12]
juros = [0, 0.1, 0.15, 0.2, 0.25]

print(f"{'Valor da Dívida':^18} {'Valor dos Juros':^18} {'Quantidade de Parcelas':^24} {'Valor da Parcela':^18}")
for i in range(len(parcelas)):
    valor = divida * (1 + juros[i])
    valor_juros = valor - divida
    qtd_parcelas = parcelas[i]
    valor_parcela = valor / qtd_parcelas
    print(f"R$ {valor:^16,.2f} R$ {valor_juros:^16,.2f} {qtd_parcelas:^23} R$ {valor_parcela:^18,.2f}")