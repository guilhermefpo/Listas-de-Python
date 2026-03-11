print('===List_Comprehension===')

# O BÁSICO

numeros = [1, 2, 3, 4, 5]
divisao = [numero / 2 for numero in numeros]
multiplicacao = [numero * 2 for numero in numeros]
potencia = [numero ** 2 for numero in numeros]

print(numeros)
print(divisao)
print(multiplicacao)
print(potencia)


# Condicionais

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novo_n = [numero for numero in n if numero > 5]
impares = [numero for numero in n if numero % 2 != 0 ]
pares = [numero for numero in n if numero % 2 == 0]
outro_if = [numero if numero != 6 else 600 for numero in n if numero % 2 == 0]
print(n)
print(novo_n)
print(impares)
print(pares)
print(outro_if)