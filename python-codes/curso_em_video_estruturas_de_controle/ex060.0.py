num = int(input('Digite um valor p/ saber seu fatorial: '))
c = num
d = num
print('{}!= {}x'.format(num,num),end='')
while c != 1:
    c -= 1
    num += (c * num) - num
    if c != 1:
        print('{}x'.format(c), end='')
    else:
        print('{}'.format(c), end='')
print(' O fatorial de {} é {}.'.format(d,num))