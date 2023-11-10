#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

dados = []

for i in range(1,6):
    id_cidade = input(f'Informe o código da {i}º cidade: ')
    numero_veiculos = int(input(f'Qual o número de veículos de passeio na {i}º cidade: '))
    numero_acidentes = int(input(f'Qualo número de acidentes com vítimas na {i}º cidade: '))

    dados.append((id_cidade,numero_veiculos,numero_acidentes))

maior_indice_acidentes = max(dados, key=lambda x: x[2])
menor_indice_acidentes = min(dados, key=lambda x: x[2])

soma_veiculos = 0
for tupla in dados:
    soma_veiculos += tupla[1]
media_veiculos = soma_veiculos / len(dados)

soma_acidentes = 0
contador = 0
for tupla in dados:
    if tupla[2] < 2000:
        soma_acidentes += tupla[2]
        contador += 1
media_acidentes = soma_acidentes / contador        

print(f"A cidade {maior_indice_acidentes[0]} possui o maior índice de acidentes: {maior_indice_acidentes[2]}")
print(f"A cidade {menor_indice_acidentes[0]} possui o menor índice de acidentes: {menor_indice_acidentes[2]}")
print(f'A média de veículos nas 5 cidades é de: {media_veiculos:,.0f}')
print(f'A média de acidentes nas cidades com menos de 2000 veículos é de: {media_acidentes:,.0f}')