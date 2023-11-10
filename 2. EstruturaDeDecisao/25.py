#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

contagem = 0

while True:
    perg1 = str(input("Telefonou para a vítima? sim ou não ")).lower()
    if perg1 == "sim":
        contagem += 1
        break
    elif perg1 == "não":
        break
    else:
        print("Entrada inválida. Por favor, digite 'sim' ou 'não' ")

while True:
    perg2 = str(input("Esteve no local do crime? sim ou não ")).lower()
    if perg2 == "sim":
        contagem += 1
        break
    elif perg2 == "não":
        break
    else:
        print("Entrada inválida. Por favor, digite 'sim' ou 'não' ")

while True:
    perg3 = str(input("Mora perto da vítima? sim ou não ")).lower()
    if perg3 == "sim":
        contagem += 1
        break
    elif perg3 == "não":
        break
    else:
        print("Entrada inválida. Por favor, digite 'sim' ou 'não' ")

while True:
    perg4 = str(input("Devia para a vítima? sim ou não ")).lower()
    if perg4 == "sim":
        contagem += 1
        break
    elif perg4 == "não":
        break
    else:
        print("Entrada inválida. Por favor, digite 'sim' ou 'não' ")

while True:
    perg5 = str(input("Ja trabalhou com a vítima? sim ou não ")).lower()
    if perg5 == "sim":
        contagem += 1
        break
    elif perg5 == "não":
        break
    else:
        print("Entrada inválida. Por favor, digite 'sim' ou 'não' ")

if contagem == 2:
    print("A pessoa é suspeita")
elif contagem == 3 or contagem == 4:
    print("A pessoa é cúmplice")
elif contagem == 5:
    print("A pessoa é assassina")
else:
    print("A pessoa é inocente")