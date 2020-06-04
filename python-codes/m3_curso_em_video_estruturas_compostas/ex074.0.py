import random
lista = tuple(random.sample(range(0,11), 5))
print('Os valores sorteados foram',end=' ')
for c in range(0,5):
    print(f'{lista[c]}',end=' ')
print(f'\nO maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')