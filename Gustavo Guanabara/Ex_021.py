print("===Radar de Velocidade==")

velocidade_carro = int(input("Qual a velocidade do carro: "))

if velocidade_carro <= 80:
    print("Você é esperto, parabéns! Não vai levar multa.")
else:
    multa = velocidade_carro - 80
    valor_multa = multa * 7
    print(f"Putz, infelizmente você foi multado em R${valor_multa:.2f}")