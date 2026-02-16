'''Dicionários'''

'''Tuplas = ()
    Listas = []
    Dicionários = {}'''

dados = {'nome':'Pedro', 'idade': 25}

dados['sexo'] = 'M'
del dados['idade']
# print(dados)

filme = {
    'titulo': 'Star Wars',
    'ano': '1977',
    'diretor': 'George Lucas'
}

'''print(filme.values())
print(filme.keys())
print(filme.items())'''

'''for k, v in filme.items():
    print(f'O {k} é {v}')'''

# Prática

pessoas = {'nome': 'Guatavo', 'sexo': 'M', 'idade': 22 }

# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

'''for k in pessoas.keys():
    print(k)'''
# pessoas['nome'] = 'Leandro'

'''pessoas['peso'] = 98.5
print(pessoas)'''

# Dicionário em lista

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
# print(brasil)
# print(brasil[0])

# print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)