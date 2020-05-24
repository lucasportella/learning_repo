a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 2
p = a1
print(a1,end=' ')
while cont <= 10:
    p += r
    print(p,end=' ')
    cont += 1
cont2 = cont
while cont > 10:
    question = int(input('\nMais termos? 0 para encerrar.'))
    if question != 0:
        while cont < cont2 + question:
            p += r
            cont += 1
            print(p,end=' ')