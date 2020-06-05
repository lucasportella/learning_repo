val = ()
valpar = 0
valparcum = ()
for c in range(0,4):
    val += (int(input('Digite um número: ')),)
    valpar = val[c]
    if valpar % 2 == 0:
        valparcum += valpar,
print(f'\nVocê digitou os valores {val}')
print(f'O valor 9 apareceu {val.count(9)} vezes.')
if 3 in val:
    print(f'Posição do primeiro 3 digitado: {val.index(3)+1}')
else:
    print('Nenhum 3 foi digitado.')
if valparcum == ():
    print('Nenhum número par foi digitado.')
else:
    print(f'Os números pares foram: {valparcum}')