# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o 
# total em segundos.  

'''d = int(input("Quantos dis?: "))
h = int(input("Quantas horas?: "))
m = int(input("Quantos minutos?: "))
s = int(input("Quantos segundos?: "))
converção1 = d * 86400
converção2 = (h * 60) * 60
converção3 = m * 60
converção = converção1 + converção2 + converção3 + s
print(f'Com base nos números apresentados, fazendo a converção temos um resultado de {converção}')'''

d = int(input("Quantos dias?: "))
h = int(input("Quantas horas?: "))
m = int(input("Quantos minutos?: "))
s = int(input("Quantos segundos?: "))

segundos_dias = d * 86400
segundos_horas = h * 3600
segundos_minutos = m * 60

total_segundos = segundos_dias + segundos_horas + segundos_minutos + s

print(f"Total em segundos: {total_segundos}")
