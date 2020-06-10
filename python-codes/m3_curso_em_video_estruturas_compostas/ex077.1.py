lista = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON',
         'CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR',
         'MERCADO','PROGRAMADOR','FUTURO')
for c in lista:
    print(f'\nNa palavra {c} temos ',end='')
    if c.count('A') >= 1:
        print('a '*c.count('A'),end='')
    if c.count('E') >= 1:
        print('e '*c.count('E'),end='')
    if c.count('I') >= 1:
        print('i '*c.count('I'),end='')
    if c.count('O') >= 1:
        print('o '*c.count('O'),end='')
    if c.count('U') >= 1:
        print('u '*c.count('U'),end='')