#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

cds = int(input("Qual a quantidade de CDs? "))
lista_cds = []

for i in range(1,cds+1):
    valor = float(input(f'Qual o valor do {i}º CD? '))
    lista_cds.append(valor)
        
total = sum(lista_cds)
media = sum(lista_cds) / len(lista_cds)

print(f'O valor total investido é de R$ {total:,.2f}\n'
      f'O valor médio gasto por CD é de R$ {media:,.2f}')