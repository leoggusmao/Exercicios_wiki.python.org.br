#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

numero = int(input("Informe um número inteiro: "))
primos = []
divisoes = 0

if numero >= 2:
    for num in range(2, numero + 1):
        is_primo = True
        for i in range(2, num):
            divisoes += 1
            if num % i == 0:
                is_primo = False
                break
        if is_primo:
            primos.append(num)

print(f'Os números primos entre 1 e {numero} são: {primos}\n'
      f'Foram realizadas {divisoes} divisões para encontrar os números primos.')
