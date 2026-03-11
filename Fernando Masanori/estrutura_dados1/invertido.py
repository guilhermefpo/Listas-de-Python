# Dado um dicionário qualquer, crie um novo dicionário onde as chaves e os valores estejam invertidos.


dic_original = {1: 'Jane', 2: 'Guilherme',3: 'Alysa'}

dic_invertido = {valor: chave for chave, valor in dic_original.items()}
print(dic_invertido)