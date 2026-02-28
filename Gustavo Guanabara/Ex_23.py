print("=== Preço da Viagem ===")

distancia = float(input("Qual foi a distância da sua viagem em Km? "))

if distancia <= 200:
    cobranca = distancia * 0.50
else:
    cobranca = distancia * 0.45

print(f'O valor da viagem foi de R${cobranca:.2f}')