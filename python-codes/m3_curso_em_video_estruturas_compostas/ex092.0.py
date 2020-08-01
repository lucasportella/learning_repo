from datetime import date

dicio = {}
dicio['Nome'] = input(str('Nome: '))

ano_atual = date.today().year
ano_nasc = int(input('Ano de Nascimento: '))
dicio['Idade'] = (ano_atual - ano_nasc)

ctps_valor = int(input('Carteira de trabalho (0 não tem): '))
if ctps_valor != 0:
    dicio['CTPS'] = ctps_valor
    dicio['Contratação'] = int(input('Ano de contratação: '))
    dicio['Salário'] = int(input('Salário R$ '))
    aposentadoria = ((dicio['Contratação']) - ano_nasc) + 35
    dicio['Aposentadoria'] = aposentadoria
print('-='*30)
for c in dicio.items():
    print(c)

