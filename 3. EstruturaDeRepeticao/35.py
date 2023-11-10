#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

numero = int(input("Informe um número inteiro: ")) #pede um númeor inteiro
primos = [] #cria a lista para adicionar os números primos

if numero >= 2: #verifica se o número é maior ou igual a dois
    for num in range(2,numero+1): #Iteração de cada item no espaço de 2 ao numero
        is_primo = True #Define a variável como verdadeira
        for i in range(2,num): #iteração de cada item no espaço de 2 ao item da iteração anterior
            if num % i == 0: #condicional para o resto da divisão do item da primeira iteração pelo item da segunda iteração
                is_primo = False #define a variável como falsa
                break #força o final da segunda iteração
        if is_primo: #condicional para verificar se a variavel é verdadeira
            primos.append(num) #adiciona o item da primeira iteração a lista

print(f'Os números primos entre 1 e {numero} são: {primos}') #mostra a lista