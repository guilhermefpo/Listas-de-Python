print("==Aluguel de carro==")

km = float(input("Quantos km o carro que foi alugado andou? "))
dias = int(input("E qual foi a quantidade de dias que esteve com ele? "))
preco_dia = 60
preco_km = 0.15
calculo_dia = preco_dia * dias
calculo_km = preco_km * km
soma_calculo = calculo_dia + calculo_km
print(f'O total a pagar é de R${soma_calculo:.2f}.')