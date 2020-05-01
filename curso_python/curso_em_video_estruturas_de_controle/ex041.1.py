from datetime import date
anonasc=int(input('Ano de nascimento: '))
anoatual=date.today().year
idade=anoatual - anonasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação Junior')
elif idade <= 20:
    print('Classificação Sênior')
elif idade > 20:
    print('Classificação Master')
