print("=== Comparando números ===")

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if n1 > n2:
    print(f'O valor {n1} é maior e o valor {n2} é menor')
elif n1 < n2:
    print(f'O valor {n2} é maior e o valor {n1} é menor')
else:
    print('Os números são iguais.')