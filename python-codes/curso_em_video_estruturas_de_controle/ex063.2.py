print('Sequência Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
t3 = t1 + t2
c = 3
print('{} → {} → {} →'.format(t1,t2,t3),end=' ')
while c < n:
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print(t3,'→',end=' ')
    c += 1
print('FIM')