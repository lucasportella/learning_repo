a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
cont2 = 0
p = a1
f = 1
print(a1, end=' ')
while f != 0:
    if cont < 10:
        a1 += r
        cont += 1
        print(a1,end=' -> ')
        if cont == 10:
            print('PAUSA')
    elif cont >= 10:
        d = int(input('\nMais termos? 0 para encerrar. '))
        cont2 += d
        if d == 0:
            print('Progressão finalizada com {} termos mostrados.'.format(cont+cont2))
            f = 0
        while a1 < (cont+cont2) * r:
            a1 += r
            print(a1,end= ' -> ')
            if a1 == ((cont+cont2)*r):
                print('PAUSA')
