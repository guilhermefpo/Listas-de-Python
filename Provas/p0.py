# . Escreva um programa que verifique se o número `42**42` é especial
# e mostre também a quantidade total de dígitos do número. Não utilize a função pronta
# `count`. Um número será chamado especial se a quantidade de dígitos 4 que aparecem na sua escrita for maior que a
# quantidade de dígitos 2.

num = 42 ** 42
text = str(num)
quant_4 = 0
quant_2 = 0

for digito in text:
    if digito == '4':
        quant_4 += 1
    if digito == '2':
        quant_2 += 1

if quant_4 > quant_2:
    print("O número é especial!")
else:
    print("O número NÃO é especial!")

print(f'Total de dígitos: {len(text)}')
print(f'Quantidade de 2: {quant_2}')
print(f'Quantidade de 4: {quant_4}')


# Gere 10 números inteiros aleatórios entre 1 e 100 e armazene-os em uma lista. Descubra
# qual é o maior número da lista sem usar as funções max, min ou sort

import random

# Gerando 10 números aleatórios
numeros = []
for _ in range(10):
    numeros.append(random.randint(1, 100))

print("Números gerados:", numeros)

# Encontrando o maior número
maior = numeros[0]
for n in numeros:
    if n > maior:
        maior = n

print("O maior número é:", maior)

#6. Peça ao usuário uma frase e gere o acrônimo, formado pelas primeiras letras de cada
# palavra em maiúsculas. Exemplo: Python para Zumbis
#→PPZ

frase = input("Escreva uma frase: ")
palavras = frase.split()
acronimo = ''
for palavra in palavras:
  acronimo += palavra[0].upper()

print(acronimo)

# Use random.randint(1, 100) para criar uma lista com exatamente 10 números sem
# repetição no intervalo de 1 a 100. Exiba a lista

import random

lista = []  # lista vazia

for _ in range(10):  
    lista.append(random.randint(1, 100))

print(lista)