#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
#O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
#Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

lista_codigo = []
lista_altura = []
lista_peso = []

while True:
    codigo = str(input('Informe seu código (0 para encerrar): '))
    if codigo == '0':
        break
    altura = float(input('Informe sua altura: '))
    peso = float(input('Informe seu peso: '))

    lista_codigo.append(codigo)
    lista_altura.append(altura)
    lista_peso.append(peso)

mais_alto = lista_altura.index(max(lista_altura))
mais_baixo = lista_altura.index(min(lista_altura))
mais_gordo = lista_peso.index(max(lista_peso))
mais_magro = lista_peso.index(min(lista_peso))

media_altura = sum(lista_altura) / len(lista_altura)
media_peso = sum(lista_peso) / len(lista_peso)

print(f'O cliente {lista_codigo[mais_alto]} é o mais alto com {max(lista_altura)} m de altura.')
print(f'O cliente {lista_codigo[mais_baixo]} é o mais baixo com {min(lista_altura)} m de altura.')
print(f'O cliente {lista_codigo[mais_gordo]} é o mais gordo com {max(lista_peso)} kg.')
print(f'O cliente {lista_codigo[mais_magro]} é o mais magro com {min(lista_peso)} kg.')
print(f'A média das alturas é de {media_altura:,.2f} m.')
print(f'A média dos pesos é de {media_peso:,.2f} kg.')