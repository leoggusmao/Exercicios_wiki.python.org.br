#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
#Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

alunos = []

for i in range(1, 11):
    numero_aluno = int(input(f"Digite o número do aluno {i}: "))
    altura = int(input(f"Digite a altura do aluno {i} em centímetros: "))
    
    alunos.append((numero_aluno, altura))

aluno_mais_alto = max(alunos, key=lambda x: x[1])
aluno_mais_baixo = min(alunos, key=lambda x: x[1])

print(f"Aluno mais alto: Número {aluno_mais_alto[0]}, Altura {aluno_mais_alto[1]} cm")
print(f"Aluno mais baixo: Número {aluno_mais_baixo[0]}, Altura {aluno_mais_baixo[1]} cm")