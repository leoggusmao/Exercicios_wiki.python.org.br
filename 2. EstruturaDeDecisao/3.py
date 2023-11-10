#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input('Informe o sexo (F) ou (M): ')
letraUp = letra.upper()

if letraUp == 'F':
    print('F - Feminino')
elif letraUp == 'M':
    print('M - Masculino')
else:
    print('Sexo Inválido')