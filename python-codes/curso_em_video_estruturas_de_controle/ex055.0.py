n=1
v = 0
v2 = 20000
for c in range(1,6,1):
    peso = float(input('Peso da {}ª pessoa em kg: '.format(n)))
    n += 1
    if v < peso:
        v = peso
    elif v2 > peso:
        v2 = peso
print('O maior peso é {} kg'.format(v))
print('O menor peso é {} kg'.format(v2))