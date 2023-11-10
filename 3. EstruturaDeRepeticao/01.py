#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nota = float(input("Dê uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        break
    else:
        print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")

print(f'Você digitou a nota {nota:.2f}')