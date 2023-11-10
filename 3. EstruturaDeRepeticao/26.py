#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input('Quantos eleitores votarão? '))
candidato_A = 0
candidato_B = 0
candidato_C = 0

for eleitor in range(1,eleitores+1):
    voto = input(f'Em qual candidato deseja votar? A, B ou C ').upper()
    if voto == "A":
        candidato_A += 1
    elif voto == "B":
        candidato_B += 1
    elif voto == "C":
        candidato_C += 1

print(f'O candidato A teve: {candidato_A:,.0f} votos\n'
      f'O candidato B teve: {candidato_B:,.0f} votos\n'
      f'O candidato C teve: {candidato_C:,.0f} votos')