num = int(input('Digite um valor p/ saber seu fatorial: '))
c = num
d = num
while c > 1:
    c += - 1
    num += (c * num) - num
print('O fatorial de {} é {}.'.format(d,num))