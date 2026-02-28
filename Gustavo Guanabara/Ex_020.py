print('===Jogo Adivinha===')

numero = int(input('Pense em um número: '))

while numero != 0:
    print("Puts não foi esse o número que pensei.")
    print("Jogue de novo!")
    numero = int(input('Pense em um número: '))

print("Parabéns eu pensei exatamente no número 0")