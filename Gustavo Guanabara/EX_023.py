print("===Maior e Menor===")

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
menor = a

# Verificando o menor valor.
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor valor digitado foi {menor}')

# verificando o maior valor.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor digitado foi o {maior}')