import math
angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem o seno de {seno:.2f}, cosseno de {cosseno:.2f} e tangente de {tangente:.2f}')