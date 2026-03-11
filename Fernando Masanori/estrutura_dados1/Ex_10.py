# Dado um dicionário, ordene-o pelos valores.

dic_original = {1: 'Jane', 2: 'Guilherme', 3: 'Alysa'}

ordenar = sorted(dic_original.items(), key=lambda x: x[1])
dic = dict(ordenar)
print(dic)