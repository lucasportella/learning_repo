ano=int(input('Digite o ano para saber se ele é bissexto (Digite 0 para saber se o ano atual é bissexto): '))
if ano == 0:
    from datetime import date
    ano = date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é Bissexto'.format(ano))