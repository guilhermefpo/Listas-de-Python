# Dada uma lista de strings contendo números misturados com letras (por exemplo, "a3b", "z12y", "c1x"), ordene a lista com base no número contido na string.

lista = ["a3b", "z6y", "c1x"]

nova_lista = sorted(lista, key=lambda x: x[1])
print(nova_lista)