from datetime import date
sexo=str(input('Você é do sexo masculino?(digite sim ou não):')).strip().upper()
if sexo == 'NÃO':
    print('Seu alistamento não é obrigatório.')
elif sexo != 'NÃO' and sexo != 'SIM':
    print('Erro. Digite apenas sim ou não.')
elif sexo == 'SIM':
    anonasc=int(input('Ano de Nascimento: '))
    anoatual = date.today().year
    idade=anoatual-anonasc
    anoalist=anonasc+18
    anorest=anoalist-(anoatual+idade)
    anosobr=(anoatual+idade)-anoalist
    if idade == 18:
        print('Você deve se alistar nesse ano({}). Não vacile.'.format(anoatual))
    elif idade > 18:
        print('\033[4;31mVocê já deveria ter se alistado. Seu alistamento foi em {}.'.format(anoalist),end=' ')
        print('Ou seja, há mais de {} ano(s).\033[m'.format(anoatual-anoalist))
    elif idade < 18:
        print('Seu alistamente será em {}. Ou seja, somente daqui há {} ano(s).'.format(anoalist,anoalist-anoatual))


