'''filme = {'título':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'
        }
for k, v in filme.items():
    print(f'O {k} é {v}.')

pessoas ={'nome': 'Gustavo','sexo': 'M', 'idade':22}
pessoas['nome'] = 'Lucas'
print(pessoas['nome'])

brasil = []
estado1 = {'uf': 'Rio de Janerio', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['sigla'])
print(brasil[1]['uf'])'''

estado = {}
brasil = []
for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

print('-='*30)
print(brasil)
print('-='*30)

for e in brasil:
    for k, v in e.items():
        print(f'{k}:',end=' ')
        print(f'{v}')
    print('------------')