# Para provas.

# 1) Contagem sem o .count():

def contar_caractere(texto, alvo):
    contador = 0
    for c in texto:
        if c == alvo:
            contador += 1
    return contador

numero = str(2**10000)
print(contar_caractere(numero, '4'))

numero = 2**10000
numero_str = str(numero)

quantidade_4 = 0
for digito in numero_str:
    if digito == '4':
        quantidade_4 += 1

print(quantidade_4)

numero = str(2**10000)
quantidade_4 = sum(1 for digito in numero if digito == '4')
print(quantidade_4)
