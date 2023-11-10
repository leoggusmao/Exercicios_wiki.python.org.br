#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome = str(input("Digite o nome de usuário: "))
    senha = str(input("Digite uma senha diferente do nome de usuário: "))
    if senha != nome:
        break
    else:
        print("ERRO! Senha inválida. Por favor, digite uma senha diferente do nome de usuário: ")