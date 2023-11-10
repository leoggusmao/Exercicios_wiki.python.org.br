#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
#Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#Maior e Menor Acerto;
#Total de Alunos que utilizaram o sistema;
#A Média das Notas da Turma.
#Gabarito da Prova:

#01 - A
#02 - B
#03 - C
#04 - D
#05 - E
#06 - E
#07 - D
#08 - C
#09 - B
#10 - A
#Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

gabarito = []
respostas = []

for i in range(1, 11):
    while True:
        resposta_gabarito = str(input(f'Informe a resposta correta da {i}º questão (A - B - C - D - E): ')).upper()
        if resposta_gabarito in ['A', 'B', 'C', 'D', 'E']:
            gabarito.append(resposta_gabarito)
            break
        else:
            print('Por favor, informe uma resposta válida (A, B, C, D ou E).')

while True:
    usar = input('Algum aluno utilizará o sistema (S ou N)? ').upper()
    if usar == "S":
        for aluno in range(1):
            nome = str(input('Informe seu nome: '))
            resposta_aluno = [nome]
            total_acertos = 0

            for i in range(1,11):
                while True:
                    resposta = str(input(f'Qual a resposta da {i}º questão (A - B - C - D - E)? ')).upper()
                    if resposta in ['A', 'B', 'C', 'D', 'E']:
                        resposta_aluno.append(resposta)
                        break
                    else:
                        print('Por favor, informe uma resposta válida (A, B, C, D ou E).')

                if resposta == gabarito[i-1]:
                    total_acertos += 1

            resposta_aluno.append(total_acertos)
            respostas.append(resposta_aluno)
    else:
        break

if respostas:
    maiores_acertos = max(respostas, key=lambda x: x[-1])
    menores_acertos = min(respostas, key=lambda x: x[-1])
    total_alunos = len(respostas)
    media_turma = sum(aluno[-1] for aluno in respostas) / total_alunos

    print(f"\nMaior Acerto: {maiores_acertos[0]} com {maiores_acertos[-1]} acertos.")
    print(f"Menor Acerto: {menores_acertos[0]} com {menores_acertos[-1]} acertos.")
    print(f"Total de Alunos: {total_alunos}")
    print(f"Média da Turma: {media_turma:.2f}")
else:
    print("Nenhum aluno utilizou o sistema.")