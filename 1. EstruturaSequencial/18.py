#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),\n
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input('Qual o tamanho do arquivo para download em MB? '))
velocidade_net = float(input('Qual a velocidade da internet em Mbps? '))
tempo_download = ((tamanho_arquivo / 8000000) / velocidade_net) * 60

print(f'O download do arquivo será completo em {tempo_download:,.8f} minutos')