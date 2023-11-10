#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
#mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

numero = int(input("Informe o número para fazer a tabuada: "))

while True:
    inicio = int(input("Informe de qual número deve começar: "))
    fim = int(input("Informe em qual número deve acabar: "))
    if inicio > fim:
        print('O número inicial deve ser menor que o final')
    else:
        break

print(f'Vou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:')
for i in range(inicio,fim+1):
    print(f'{numero} x {i} = {numero * i}')