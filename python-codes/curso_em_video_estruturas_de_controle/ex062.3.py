a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
c2 = 10
d = 0
while d == 0:
    while c < 10:
        print(a1,end=' -> ')
        a1 += r
        c += 1
    if c == c2:
        c2 += int(input('PAUSA \nMais termos? 0 para encerrar. '))
        if c2 == c:
            d = 1
    while c < c2:
        print(a1,end=' -> ')
        c += 1
        a1 += r
if d == 1:
    print('FIM')
    print('Total de termos:',c)

