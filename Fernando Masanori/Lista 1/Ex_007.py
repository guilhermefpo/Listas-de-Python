# 7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32 8) Faça agora o 
# contrário, de Fahrenheit para Celsius.  

'''print('==Converção==')

celsius = float(input("Digite a temperatura condizente: "))
conversor_fahrenheit = (9/5) * celsius + 32
fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
conversor_celsius = (fahrenheit - 32) * 5 / 9
print(f'Celsius para Fahrenheit: {conversor_fahrenheit}°F')
print(f'Fahrenheit para Celsius: {conversor_celsius:.2f}°C')'''

print('== Conversão de Temperaturas ==')

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (9 * celsius / 5) + 32
print(f'Celsius para Fahrenheit: {fahrenheit:.2f}°F')

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f'Fahrenheit para Celsius: {celsius:.2f}°C')

