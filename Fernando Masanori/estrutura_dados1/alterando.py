# Dada uma string, utilize list comprehension para criar uma nova string onde os caracteres aparecem alternando entre maiúsculas e  minúsculas.
# nova_lista = "".join([letra.upper() if indice % 2 == 0  else letra.lower() for letra , indice in enumerate(palavra)])
palavra = "Guilherme"

nova_string = "".join(
    letra.upper() if indice % 2 == 0 else letra.lower()
    for indice, letra in enumerate(palavra)
)

print(nova_string)
