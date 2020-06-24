tupla1 = ()
for c in range(4):
    tupla1 += int(input('Digite um número: ')),
print(f'O número 9 apareceu {tupla1.count(9)} vezes.')
if 3 in tupla1:
    print(f'O número 3 apareceu pela 1ª vez na posição {tupla1.index(3)+1}.')
print('Números pares digitados: ',end='')
for c in tupla1:
    if c % 2 == 0:
        print(f'{c} ',end='')