print("==Reajuste Salarial==")

salario = float(input("Qual é o salário do funcionário? "))
aumento = 15/100
ajuste = salario * aumento
salario_novo = salario + ajuste
print(f'Após o aumento o salário do funcionário que antes era de R${salario:.2f}, agora passou a ser R${salario_novo:.2f}, com o aumento de 15%')