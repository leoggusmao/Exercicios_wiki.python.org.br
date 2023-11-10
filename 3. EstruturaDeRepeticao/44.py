#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#1, 2, 3, 4  - Votos para os respectivos candidatos 
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

print("Candidatos:\n1 - Lula\n2 - Bolsonaro\n3 - Marina\n4 - Ciro\n5 - Nulo\n6 - Branco")

votos = [[], [], [], [], [], []]
qtd = 0

while True:
    voto = int(input("Informe o seu voto (ou 0 para encerrar): "))
    qtd += 1
    if voto == 0:
        break

    if voto == 1:
        votos[0].append(voto)
    elif voto == 2:
        votos[1].append(voto)
    elif voto == 3:
        votos[2].append(voto)
    elif voto == 4:
        votos[3].append(voto)
    elif voto == 5:
        votos[4].append(voto)
    elif voto == 6:
        votos[5].append(voto)

print(f"Lula: {len(votos[0])}\nBolsonaro: {len(votos[1])}\nMarina: {len(votos[2])}\nCiro: {len(votos[3])}")
print(f"Votos nulos: {len(votos[4])}, representam {(len(votos[4])/qtd)*100:,.2f}% do total de votos")
print(f"Votos em branco: {len(votos[5])}, representam {(len(votos[5])/qtd)*100:,.2f}% do total de votos")    