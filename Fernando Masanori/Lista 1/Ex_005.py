# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço 
# a pagar. 

mercadoria = float(input("Qual o valor da mercadoria?: "))
percentual = float(input("Qual o desconto do produto?: "))

desconto = mercadoria * (percentual / 100)
ajuste = mercadoria - desconto

print(f"O desconto é de R${desconto:.2f}")
print(f"O preço a pagar pela mercadoria será de R${ajuste:.2f}")
