#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = str(input("Digite o nome (mais de 3 caracteres): "))
    contador = 0
    for i in nome:
        if i.isalpha():
            contador += 1
    if contador > 3:
        break
    else:
        print("O nome deve conter mais de 3 caracteres, tente novamente.")

while True:
    idade = int(input("Informe a idade: "))
    if 0 <= idade <= 150:
        break
    else:
        print("A idade deve estar entre 0 e 150.")

while True:
    salario = float(input("Informe o salário: "))
    if salario > 0:
        break
    else:
        print("O salário deve ser maior que 0")

while True:
    sexo = str(input("Qual o sexo: F - feminino   M - masculino ")).upper()
    if sexo == 'F' or sexo == 'M':
        break
    else:
        print("Entrada inválida. Digite F ou M")

while True:
    estado_civil = str(input("Qual o estado civil: S- solteiro  C- casado  V- viúvo  D- divorciado ")).upper()
    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':
        break
    else:
        print("Entrada inválida. Digite S, C, V ou D")

print(f'Nome: {nome}\n'
      f'Idade: {idade}\n'
      f'Salário: R$ {salario:,.2f}\n'
      f'Sexo: {sexo}\n'
      f'Estado civil: {estado_civil}')