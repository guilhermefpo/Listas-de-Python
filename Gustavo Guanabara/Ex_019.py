print('==Primeiro e Ultimo==')

nome = str(input('Digite seu nome completo: '))
separa = nome.split()

print(f'Seu primeiro nome é {separa[0]}')
print(f'Seu ultimo nome é {separa[-1]}')
