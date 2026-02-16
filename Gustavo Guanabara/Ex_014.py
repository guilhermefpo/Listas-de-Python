print('==Catetos e Hipotenusa==')

cateto1 = int(input('Digite o valor de um dos catetos: '))
cateto2 = int(input('Agora digite o valor de outro cateto: '))
calculo = (cateto1 ** 2) + (cateto2 ** 2)
calc = calculo ** (1/2)
print(f'A hipotenusa é igual a {calc}.')