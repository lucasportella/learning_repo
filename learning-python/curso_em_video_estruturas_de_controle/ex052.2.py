num=int(input('Digite um número: '))
cont = 0
cont2 = 1
for c in range(1,11,1):

    if (num % c == 0):
        print('\033[1;36m{}\033[m'.format(c),end=' ')
        cont += 1
        cont2 += 1
    elif (num % c != 0):
        print('\033[0;31m{}\033[m'.format(c),end=' ')

if num <= 7 and cont >= 3:
    print('O número {} foi divido {} vez(es)!'.format(num, cont))
    print('O número {} NÃO é primo!'.format(num))
elif 8 <= num <= 10 and cont2 >=2:
    print('O número {} foi divido {} vez(es)!'.format(num, cont))
    print('O número {} NÃO é primo!'.format(num))
elif num >=11 and cont2 > 2:
    print('O número {} NÃO é primo!'.format(num))
    print('O número {} foi divido {} vez(es)!'.format(num, cont2))
else:
    print('\nO número {} é primo!'.format(num))
    print('O número {} foi divido {} vez(es)!'.format(num, cont2))