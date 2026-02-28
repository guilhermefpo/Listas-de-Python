# Dada uma lista de palavras, ordene-a pelo último caractere de cada palavra.

lista = ['Abacate', 'Pera', 'Morango']

ultimo_car = sorted(lista, key=lambda x: x[-1])

print(ultimo_car)