lista = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
vogais = ('A','E','I','O','U')
for l in lista:
    print(f'\nNa palavra {l} temos',end=' ')
    for v in vogais:
        if v in l:
            print(v*l.count(v),end=' ')

