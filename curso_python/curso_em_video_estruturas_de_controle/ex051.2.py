a1=float(input('Digite o primeiro termo da PA: '))
r=float(input('Digite a razão da PA: '))
for c in range(1,11):
    a1 += r
    print('{:.2f}'.format(a1), end=' -> ')
print('FIM')
