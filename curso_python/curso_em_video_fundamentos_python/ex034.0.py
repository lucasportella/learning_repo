sal = float(input('Salário do funcionário: R$ '))
if sal > 1250.00:
    print('\033[33mO salário com aumento ficará {:.2f}R$\033[m'.format((sal * 0.1) + sal))
else:
    print('\033[4;34;46mO salário com aumento ficará {:.2f}R$\033[m'.format((sal * (15 / 100)) + sal))
