print("== Conversor de Temperatura ==")

temperatura_celsius = float(input("Quantos graus está fazendo hoje? "))
conversor_f = (9/5) * temperatura_celsius + 32

print(f"A temperatura convertida de {temperatura_celsius}°C para Fahrenheit é de {conversor_f:.2f}°F.")
