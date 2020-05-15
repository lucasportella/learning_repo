p1 = int(input('Primeiro termo: '))
p = p1
r = int(input('Razão: '))
while p1 < (p + r*10):
    print(p1, '->', end=' ')
    p1 += r
print('Fim')