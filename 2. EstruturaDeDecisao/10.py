#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.\n
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Qual turno você estuda? M - matutino ou V - vespertino ou N - noturno ').upper()

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite')
else:
    print('Valor Inválido!')