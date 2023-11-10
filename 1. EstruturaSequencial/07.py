#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Informe o tamanho em metros do lado de um quadrado: '))
area_quadrado = lado ** 2
print(f'O dobro da área do quadrado é {2 * area_quadrado:,.2f} metros quadrados')