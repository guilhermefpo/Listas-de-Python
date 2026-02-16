print('==Analisador de Textos==')

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome maiusculo: {nome.upper()}')
print(f'Seu nome minusculo: {nome.lower()}')
print(f'Seu nome tem: {len(nome) - nome.count(' ')} letras')
# print(f'Seu primeiro nome tem: {nome.find(' ')} letras.')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras.')