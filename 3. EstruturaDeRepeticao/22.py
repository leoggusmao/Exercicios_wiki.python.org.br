#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

numero = int(input("Informe um número: "))
divisores =[]

if numero > 1:
    primo = True
    for i in range(2,numero):
        if numero % i == 0:
            primo = False
            divisores.append(i)
    
    if primo:
        print(f"O número {numero} é primo")
    else:
        print(f"O número {numero} não é primo")
        print(f'Os números: {divisores}, são divisores')
else:
    print(f"O número {numero} não é primo")
    print(f'Os números: {divisores}, são divisores')