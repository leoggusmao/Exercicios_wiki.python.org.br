#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

quantidade_turmas = int(input("Qual a quantidade de turmas? "))
lista_turmas = []

for t in range(1,quantidade_turmas+1):
    while True:
        alunos = int(input(f'Qual a quantidade de alunos na {t}º turma? '))
        if alunos > 40:
            print("A turma não pode ter mais de 40 alunos")
        else:
            lista_turmas.append(alunos)
            break
        
media = sum(lista_turmas) / len(lista_turmas)

print(f'O número médio de alunos por turma é {media:,.0f}')