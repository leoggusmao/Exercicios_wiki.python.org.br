#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

qtd_morango = float(input("Qual a quantidade em Kg de morangos? "))
qtd_maca = float(input("Qual a quantidade em Kg de maçãs? "))
qtd_total = qtd_morango + qtd_maca

if qtd_morango <= 5:
    valor_morango = 2.5 * qtd_morango
else:
    valor_morango = 2.5 * qtd_morango

if qtd_maca <= 5:
    valor_maca = 1.8 * qtd_maca
else:
    valor_maca = 1.5 * qtd_maca

valor_total = valor_morango + valor_maca

if qtd_total > 8 or valor_total > 25:
    valor_total *= 0.9

print(f'O valor para a compra de {qtd_morango:,.0f} kg de morangos e {qtd_maca:,.0f} kg de maçãs é de R$ {valor_total:,.2f}')