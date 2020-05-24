total = int(input('Valor de saque: R$'))
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced != 0:
            print(f'{totced} nota(s) de R${ced}')
        if total < 50 and total >= 20:
            ced = 20
            totced = 0
        elif total < 20 and total >= 10:
            ced = 10
            totced = 0
        elif total < 10 and total >= 1:
            ced = 1
            totced = 0
        elif total == 0:
            break