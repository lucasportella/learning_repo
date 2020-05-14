'''fazer com if dentro do print
fazer com recebe multiplicação *= ou x = x * y'''
num = int(input('Digite um valor p/ ver seu fatorial: '))
c = num - 1
d = num
f = num + 1
while c > 0:
    num *= c
f -= 1
    print('{} x '.format(f) if f > 2 else '2 x 1 = {}'.format(num),end='')
    c -= 1
print('\nFatorial de {}! = {}'.format(d,num) if d != 0 else 'Fatorial de 0! = 1')

