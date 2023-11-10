#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:
    A = int(input("Informe o número de habitantes do país A: "))

    while True:
        B = int(input("Informe o número de habitantes do país B: "))
        if B > A:
            break
        else:
            print("O valor de B deve ser maior que A.")

    tx_A = float(input("Informe a taxa de crescimento de A (em %): ")) / 100

    while True:
        tx_B = float(input("Informe a taxa de crescimento de B (em %): ")) /100
        if tx_B < tx_A:
            break
        else:
            print("A taxa de crescimento de B deve ser menor que a de A.")

    anos = 0

    while A < B:
        A += A * tx_A
        B += B * tx_B
        anos += 1

    print(f'Levará {anos} anos para a população de A ultrapassar ou igualar a população de B.')

    repetir = input("Deseja repetir a operação? (S para sim, qualquer outra tecla para sair): ").upper()
    if repetir != "S":
        break
