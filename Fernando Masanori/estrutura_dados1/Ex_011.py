# Dada uma frase, crie um dicionário onde as chaves são palavras e os valores são a contagem de vezes que cada palavra aparece.


dic = 'Guilherme vai a fera'

dic_frase = {palavra: dic.split().count(palavra) for palavra in set(dic.split())}
print(dic_frase)