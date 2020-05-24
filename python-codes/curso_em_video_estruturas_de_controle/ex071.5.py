saque = int(input('Valor do saque: '))
for notas in [50, 20, 10, 1]:
    quant = saque // notas
    print(f'{quant} notas de {notas}')
    saque %= notas
