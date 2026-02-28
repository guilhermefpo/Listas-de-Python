# Para lista

numeros = [1, 2, 3, 4]
# Lista com os quadrados só com os pares.
quadrados = [x**2 for x in numeros if x % 2 == 0]
print(quadrados)

# Para dicionario
notas = {'Ana': 5, 'Pedro': 8, 'Luiz': 9, 'Chico': 7}
condicao = {x for x in notas if notas[x] > 5}
print(condicao)

# Lambda
nomes = 'pedro camila arthur jose'.split()
n1 = sorted(nomes)
n2 = sorted(nomes, key=len)

def segunda(nome): return nome[1]

segunda(nomes)