# Dada uma lista de palavras, ordene-a pelo número de vogais presentes em cada palavra.

lista = ['Abacate', 'Pera', 'Churros', 'Goiaba', 'Pessego']

vogais = sorted(lista, key=lambda x: sum(1 for letra in x.lower() if letra in 'aeiou'))

print(vogais)
