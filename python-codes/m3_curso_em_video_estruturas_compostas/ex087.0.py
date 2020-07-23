lista = [[0,1,2],[0,1,2],[0,1,2]]
parsom = 0
imparsom = 0
maior_valor_seg_linha = int()
for c in range(3):
    for d in range(3):
        lista[c][d] = int(input(f'Digite um valor para [{c},{d}]: '))
        if lista[c][d] % 2 == 0:
            parsom += lista[c][d]
        if d == 2:
            imparsom += lista[c][d]
        if c == 1 and lista [c][d] > maior_valor_seg_linha:
            maior_valor_seg_linha = lista[c][d]
print('-'*60)
for c in range(3):
    for d in range(3):
            print(f'[{lista[c][d]:^5}]',end='')
    print()
print('-'*60)
print(f'A soma dos valores pares é {parsom}')
print(f'A soma dos valores da terceira coluna é {imparsom}')
print(f'O maior valor da segunda linha é {maior_valor_seg_linha}')
