# 9) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a 
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante 
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o 
# total de dias. 

'''print('==Cigarros==')

cigarros = int(input("Quantos cigarros você fuma por dia? "))
tempo = int(input("Por quantos anos o senhor fuma? "))
ano = 525600
dia = 1440
calculo_tempo = ano * tempo
calculo = calculo_tempo / dia
total_cigarros = cigarros * tempo * 365
total_minutos_perdidos = total_cigarros * 10
dias_perdidos = total_minutos_perdidos / 1440'''

print('==Cigarros==')

cigarros = int(input("Quantos cigarros você fuma por dia? "))
tempo = int(input("Por quantos anos o senhor fuma? "))

# Total de cigarros fumados
total_cigarros = cigarros * tempo * 365

# Cada cigarro tira 10 minutos de vida
total_minutos_perdidos = total_cigarros * 10

# Converter minutos perdidos em dias
dias_perdidos = total_minutos_perdidos / 1440

print(f'O total de dias de vida perdidos é: {dias_perdidos:.2f}')
