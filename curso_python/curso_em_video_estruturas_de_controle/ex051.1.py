a1=int(input('Primeiro termo: '))
r=int(input('Razão: '))
print('Os 10 primeiros termos da PA são: \n{}->'.format(a1),end=' ')
for c in range(a1,(a1+9*r),r):
    a1 = a1 + r
    print(a1, end=' -> ')
print('FIM')
