for c in range(1,6,1):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    elif c > 1:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('A pessoa mais pesada tem {} kg'.format(maior))
print('A pessoa mais leve tem {} kg'.format(menor))