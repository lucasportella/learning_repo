from datetime import date
anoatual= date.today().year
anonasc=int(input('Ano de nascimento: '))
anoalist=anonasc+18
idade=anoatual-anonasc
restanos=anoalist-(anonasc+idade)
if anonasc == anoatual:
    print('Quem nasceu neste ano, deve se alistar daqui a 18 anos.')
else:
    print('Quem nasceu em {} tem ou terá, em breve, {} ano(s) em {}.'.format(anonasc,idade,anoatual))
if anonasc == (anoatual-18):
    print('Voce deve se alistar nesse ano. Não vacile.')
elif anonasc > anoatual-18:
    print('Você deverá se alistar em {}.'.format(anoalist))
elif anonasc < anoatual-18:
    print('\033[4;31mO seu tempo de alistamento já passou. Você deveria ter se alistado em {}.\033[m'.format(anoalist))
