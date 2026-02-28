# Crie uma lista com os quadrados de todos os números pares de 1 a 20 usando list comprehension.

'''lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

quadrados = [ x**2 for x in lista if x % 2 == 0 ]'''

quadrados = [x**2 for x in range(1, 21) if x % 2 == 0]
print(quadrados)
