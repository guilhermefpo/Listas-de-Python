# Dada uma string, crie um dicionário onde as chaves são os caracteres e os valores são a contagem de vezes que cada caractere # aparece.

texto = 'Os cachorros  foram  passear na rua'

disc = {letra: texto.count(letra)  for letra in set(texto)}
print(disc)