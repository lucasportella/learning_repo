num = int(input('Digite um número: '))
cont = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[34m{}\33[m'.format(c),end=' ')
        cont += 1
    else:
        print('\033[35m{}\033[m'.format(c),end=' ')
if cont == 2:
    print('\nO número {} é primo!'.format(num))
else:
    print('\nO número {} NÃO é primo!'.format(num))
