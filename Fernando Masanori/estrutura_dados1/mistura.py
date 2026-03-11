# Dada uma lista de strings contendo números misturados com letras (por exemplo, "a3b", "z12y", "c1x"), ordene a lista com base no número contido na string.

lista = ["a3b", "z6y", "c12x"]

nova_lista = sorted(lista, key=lambda x: int(''.join([c for c in x if c.isdigit()])))

print(nova_lista)