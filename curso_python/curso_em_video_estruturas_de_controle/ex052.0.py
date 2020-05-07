num = int(input('Digite um número: '))
if num == 2 or num == 3 or num == 5 or num == 7:
    print('O número {} é primo!'.format(num))
elif num % 2 == 0:
    print('O número {} NÃO é primo!'.format(num))
elif num % 3 == 0:
    print('O número {} NÃO é primo!'.format(num))
elif num % 5 == 0:
    print('O número {} NÃO é primo!'.format(num))
elif num % 7 == 0:
    print('O número {} NÃO é primo!'.format(num))
elif num % 2 and 3 and 5 and 7 != 0:
    print('O número {} é primo!'.format(num))