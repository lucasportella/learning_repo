saque = int(input('Valor do saque:'))
ced = 50
totced = 0
while True:
    if saque >= ced:
        saque -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} notas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if saque == 0:
            break

