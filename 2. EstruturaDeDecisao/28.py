#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
#Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
#Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

while True:
    tipo = input("Qual o tipo de carne deseja comprar? F - filé   A - alcatra   P - picanha ").upper()
    if tipo == "F" or tipo == "A" or tipo == "P":
        break
    else:
        print("Entrada inválida! Por favor, digite F - filé   A - alcatra   P - picanha ")

qtd = float(input("Qual a quantidade deseja comprar? "))

if tipo == "F" and qtd <= 5:
    valor = 4.9 * qtd
elif tipo =="F" and qtd > 5:
    valor = 5.8 * qtd
elif tipo == "A" and qtd <= 5:
    valor = 5.9 * qtd
elif tipo == "A" and qtd > 5:
    valor = 6.8 * qtd
elif tipo == "P" and qtd <= 5:
    valor = 6.9 * qtd
else:
    valor = 7.8 * qtd

while True:
    pagamento = input("Deseja utilizar o cartão Tabajara? S - sim   N - não ").upper()
    if pagamento == "S" or pagamento == "N":
        break
    else:
        print("Entrada inválida! Por favor, digite S - sim ou N - não")

if pagamento == "S":
    valor_desconto = valor * 0.05
    valor *= 0.95
elif pagamento =="N":
    valor_desconto = 0

print(f'Tipo:                                          : {tipo}\n'
      f'Quantidade (Kg)                                : {qtd:,.2f}\n'
      f'Preço Total                                    : R$ {valor:,.2f}\n'
      f'Cartão Tabajara                                : {pagamento}\n'
      f'Valor do desconto                              : R$ {valor_desconto:,.2f}\n'
      f'Valor a pagar                                  : R$ {valor:,.2f}')