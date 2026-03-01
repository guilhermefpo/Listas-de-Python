print('=== LISTAS ===')

# Criando uma lista inicial
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']

# Alterando um elemento da lista (posição 3)
lanche[3] = 'Picolé'
print(lanche)

# Adicionando um item no final da lista
lanche.append('Salada')
print(lanche)

# Inserindo um item em uma posição específica (posição 0)
lanche.insert(0, 'Cachorro Quente')
print(lanche)

# Deletando um item pelo índice (posição 3)
del lanche[3]
print(lanche)

# Remove o último elemento da lista
lanche.pop()
print(lanche)

# Remove elemento de uma posição específica (posição 3)
lanche.pop(3)
print(lanche)

# Remove um elemento pelo nome (valor)
lanche.remove('Cachorro Quente')
print(lanche)

# Verificando se um item existe antes de remover
if 'Pizza' in lanche:
    lanche.remove('Pizza')
    print(lanche)
else:
    print('Putz não deu!')
    print(lanche)

# Criando lista automaticamente com range (1 até 10)
valores = list(range(1, 11))
print(valores)

# Criando outra lista numérica
val = [8, 2, 7, 4, 5, 9, 3, 0]

# Ordenando em ordem crescente
val.sort()
print(val)

# Ordenando em ordem decrescente
val.sort(reverse=True)
print(val)

# Mostrando o tamanho da lista
n = len(val)
print(n)

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])