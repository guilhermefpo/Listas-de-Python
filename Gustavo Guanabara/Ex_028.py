print('===Soma multiplos de 3===')

'''soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0 :
      soma += c

print(f'A soma de todos os números é {soma}')'''

soma = 0
for c in range(3, 501, 6):  # começa em 3, pula de 6 em 6 (somente ímpares múltiplos de 3)
    soma += c
print(f'A soma de todos os números é {soma}')
