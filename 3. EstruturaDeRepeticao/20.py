#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.


while True:
    ativar = input("Gostaria de realizar a fatoração? S - sim   Qualquer tecla - não ").upper()
    
    if ativar == "S":
        while True:
            numero = int(input("Informe um número inteiro para fatoração: "))
            fatoracao = 1
            etapas = ''
            if 0 < numero < 16: 
                for i in range(1, numero + 1):
                    fatoracao *= i
                    etapas += str(i)
                    if i < numero:
                        etapas += ' * '

                print(f'{numero}! = {etapas} = {fatoracao}')
                break
            else:
                print("O número deve ser inteiro, positivo e menor que 16")

    elif ativar != "S":
        print("Obrigado por nada!")
        break