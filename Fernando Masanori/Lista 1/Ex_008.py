# 8) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo 
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. 

km = float(input("Quantos km o carro percorreu? "))
dias = int(input("Por quantos dias o carro foi alugado? "))

total = (dias * 60) + (km * 0.15)

print(f"O total a pagar é R${total:.2f}")
