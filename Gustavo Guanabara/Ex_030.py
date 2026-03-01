print('===Soma Pares===')

'''soma = 0
for c in range(1, 7):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        soma = n + soma
    else: 
        soma = soma + 0
print(f'Soma: {soma}')'''

soma = 0
for c in range(1, 7):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        soma += n

print(f'Soma: {soma}')


