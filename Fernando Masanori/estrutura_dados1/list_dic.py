# Crie um dicionário que mapeia os números de 1 a 10 para seus respectivos quadrados, usando dict comprehension.

dic = {"n1": 1, "n2": 2, "n3": 3, "n4": 4, "n5": 5, "n6": 6, "n7": 7, "n8": 8, "n9": 9, "n10": 10}
nova_dic = {pow(x, 2) for x in dic}
print(nova_dic)