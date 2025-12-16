print("=== Pintando Parede ===")

'''largura = int(input("Qual a largura da sua parede?: "))
altura = int(input("E qual a altura da sua parede?: "))
area = altura * largura
tinta = area/2

print(f'Para uma área de {area:.2f} metros quadrados, o total de tinta a se ultilizar é igual a {tinta:.2f} litros de tinta.')'''

largura = float(input("Qual a largura da sua parede (em metros)? "))
altura = float(input("Qual a altura da sua parede (em metros)? "))

area = largura * altura
cobertura_por_litro = 2  # 1 litro cobre 2 m²
tinta = area / cobertura_por_litro

print(f"\nÁrea total: {area:.2f} m²")
print(f"Tinta necessária: {tinta:.2f} litros")
