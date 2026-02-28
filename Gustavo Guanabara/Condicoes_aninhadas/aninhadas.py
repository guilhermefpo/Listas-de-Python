nome = str(input("Qual é seu nome: "))

if nome == "Alysa":
    print("Que nome bonito!")
elif nome == "Guilherme" or nome == "Gustavo":
    print("Seu nome é bem popular no Brasil!")
else:
    print("Seu nome é bem normal!")
print(f'Tenha um bom dia {nome}')