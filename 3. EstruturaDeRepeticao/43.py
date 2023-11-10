#O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,18
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,18
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

cardapio = [[100, 'Cachorro Quente', 1.2], [101, 'Bauru Simples', 1.3], [102, 'Bauru com ovo', 1.5], [103, 'Hambúrguer', 1.2], [104, 'Cheeseburguer', 1.3], [105, 'Refrigerante', 1]]
pedido = []

while True:
    codigo = int(input('Informe o código do item desejado (ou 0 para encerrar): '))
    if codigo == 0:
        break
    quantidade = int(input('informe a quantidade desejada: '))
    pedido.append((codigo, quantidade))

total_pedido = 0

print(f"{'Especificação':^18} {'Código':^18} {'Preço':^18} {'Quantidade':^18} {'Total':^18}")
for item in pedido:
    for produto in cardapio:
        if item[0] == produto[0]:
            especificacao = produto[1]
            preco = produto[2]
            qtd = item[1]
            total_item = preco * qtd
            total_pedido += total_item
            print(f"{especificacao:^18} {item[0]:^18} {preco:^18.2f} {qtd:^18} R$ {total_item:^18.2f}")

print(f'Total do Pedido: R$ {total_pedido:.2f}')