a1=float(input('Digite o primeiro termo da PA: '))
r=float(input('Digite a razão da PA: '))
print('Os 10 primeiros termos dessa PA são: \n{} ->'.format(a1),end=' ') #toda essa ganbiarra aqui necessárioa pq não inverti a linha 5 e 6
for c in range(1,10):
    a1 += r
    print('{:.2f}'.format(a1), end=' -> ')
print('FIM')
