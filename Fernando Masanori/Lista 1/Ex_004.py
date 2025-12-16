# 4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a 
# porcentagem do aumento. Exiba o valor do aumento e do novo salário. 

salario = float(input("Qual o seu salário atual?: "))
aumento = int(input("Qual o valor da porcentagem desse aumento?: "))
ajuste = salario / aumento
ajuste_salarial = salario + ajuste
print(f'O valor do seu aumento será de R${ajuste}, o valor após o aumento será de R${ajuste_salarial}')