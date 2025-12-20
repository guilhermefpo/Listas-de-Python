print("==Calculando Desconto==")

valor_produto = float(input("Qual o valor do produto? "))
desconto = 5/100
ajuste = valor_produto * desconto
valor_final = valor_produto - ajuste
print(f'Para esse produto de R${valor_produto} o desconto é de 5%, portanto, o valor final a ser pago é de R${valor_final:.2f}')