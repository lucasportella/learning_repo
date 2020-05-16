print('Sequência Fibonacci')
n = int(input('Digite o termo desejado da sequência: '))
t1 = 0
t2 = 1
t3 = t1 + t2
c = 3
if n == 1:
    print(t1)
elif n == 2:
    print(t1,'→', t2)
elif n > 2:
    print(t1,'→', t2,'→', t3, end = ' → ')
    while c < n:
        c += 1
        t1 = t2
        t2 = t3
        t3 = t1 + t2
        print(t3,end=' → ')
print('FIM')