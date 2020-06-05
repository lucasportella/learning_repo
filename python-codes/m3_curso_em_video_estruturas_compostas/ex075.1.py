val = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {val}')
print(f'O valor 9 apareceu {val.count(9)} vezes.')
if 3 in val:
    print(f'A primeira posição do valor 3 foi a posição {val.index(3)+1}.')
else:
    print('O valor 3 não foi digitado.')
print(f'Valores pares digitados:',end=' ')
for c in val:
    if c % 2 == 0:
        print(c,end=' ')
