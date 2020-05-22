s = maisdemil = maisbarato = 0
maisbaratonome = ' '
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço: R$'))
    s += preço
    if preço > 1000:
        maisdemil += 1
    if maisbarato == 0:
        maisbarato = preço
        maisbaratonome = produto
    elif preço < maisbarato:
        maisbarato = preço
        maisbaratonome = produto
    continuar = ' '
    while continuar not in 'NNÃONAOSSIM':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()
    if continuar in 'NNÃONAO':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${s:.2f}')
print(f'Temos {maisdemil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {maisbaratonome.capitalize()} que custa R${maisbarato:.2f}')
