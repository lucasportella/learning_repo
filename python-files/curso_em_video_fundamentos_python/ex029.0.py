vel=float(input('Velocidade registrada em km/h: '))
multa=(vel - 80)*7
print('A velocidade registrada foi de {} km/h'.format(vel))
if vel <= 80:
    print('\033[1;33mA velocidade de tráfego está regular, nenhuma multa a ser aplicada')
else:
    print('\033[1;31mA velocidade de tráfego está excessiva, valor da multa é de R${:.2f}'.format(multa))