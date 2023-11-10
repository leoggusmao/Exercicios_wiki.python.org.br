#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
#Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input("Informe um número: "))

if numero > 1:
    primo = True
    for i in range(2,numero):
        if numero % i == 0:
            primo = False
            break
    
    if primo:
        print(f"O número {numero} é primo")
    else:
        print(f"O número {numero} não é primo")
else:
    print(f"O número {numero} não é primo")