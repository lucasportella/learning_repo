print('Considerando que estamos no ano de 2017...')
ano=int(input('Ano de nascimento: '))
idade=int(2017-ano)
idadextra=idade-18
anoalist=ano+18
print('Quem nasceu em {} tem ou terá, em breve, {} ano(s) em 2017.'.format(ano,(int(2017)-ano)))
if ano == int(1999):
    print('Seu alistamento militar deve ser feito neste ano. Não vacile.')
elif ano < int(1999):
    print('Você já deveria ter se alistado há {} ano(s).'.format(idade-(2017-1999)))
    print('\033[1;31mSeu alistamento foi em {}. Regularize-se!\033[m'.format((idade-idadextra)+ano))
elif ano > int(1999):
    print('Ainda falta {} ano(s) para o alistamento.'.format(anoalist-(ano+idade)))
    print('Seu alistamento será em {}.'.format(anoalist))