#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
#e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

quantidade_pessoas = int(input("Quantas pessoas estão na turma? "))
lista_idades = []

for i in range(1,quantidade_pessoas+1):
    idade = int(input(f'Qual a idade da {i}º pessoa? '))
    lista_idades.append(idade)

media_idades = sum(lista_idades) / len(lista_idades)

if 0 <= media_idades <= 25:
    print("A turma é jovem.")
elif 25 < media_idades <= 60:
    print("A turma é adulta.")
else:
    print("A turma é velha.")