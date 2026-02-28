print("===Aprovando Empréstimos===")

valor_casa = float(input("Qual o valor da casa?: "))
salario_comprador = float(input("Qual o sálario do comprador?: "))
anos = int(input("Em quantos anos serão pagos?: "))
prestacao = valor_casa / (anos * 12)
minimo = salario_comprador * 30 / 100
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos.')
print(f'A prestação será de R${prestacao:.2f}')

if prestacao <= minimo:
    print(f'Empréstimo pode ser concedido!')
else:
    print(f'Emprestimo negado!')