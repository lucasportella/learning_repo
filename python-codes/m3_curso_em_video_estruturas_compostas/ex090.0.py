dicio = {}
dicio['Nome'] = str(input('Nome: '))
dicio['Média'] = float(input(f'Média de {dicio["Nome"]}: '))
if dicio['Média'] >= 7.0:
    dicio['Situação'] = str('Aprovado')
else:
    dicio['Situação'] = str('Reprovado')
print('-='*30)

for k, v in dicio.items():
    print(k, v)