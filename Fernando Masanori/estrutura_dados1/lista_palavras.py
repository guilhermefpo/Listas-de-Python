# Dada uma lista de palavras, ordene-a pelo tamanho das palavras em ordem crescente, utilizando sorted() com a cláusula key=.

lista = ['Música', 'Abacate', 'Vôlei', 'Programação']

ordenar = sorted(lista, key=len)
print(ordenar)

'''
lista = ['Música', 'Abacate', 'Vôlei', 'Programação']

ordenar_desc = sorted(lista, key=len, reverse=True)
print(ordenar_desc)
Do maior para o menor.
'''