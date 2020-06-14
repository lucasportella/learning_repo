lista1 = []
maior = 0
menor = 0
for c in range(0,5):
    lista1.append(int(input(f'Digite o {c+1}º número: ')))
    if c == 0:
        maior = menor = lista1[c]
    else:
        if lista1[c] > maior:
            maior = lista1[c]
        if lista1[c] < menor:
            menor = lista1[c]
print(f'O maior número digitado foi {maior} na(s) posição(ões):',end=' ')
for p, e in enumerate(lista1):
    if e == maior:
        print(f'{p}º',end=' ')
print(f'\nO menor número digitado foi {menor} na(s) posição(ões):',end=' ')
for p, e in enumerate(lista1):
    if e == menor:
        print(f'{p}º',end=' ')
