num = int(input('Digite um valor para saber seu fatorial: '))
d = num
for c in range(num-1,1,-1):
    num += (num * c) - num
print('O fatorial de {} é {}.'.format(d, num))