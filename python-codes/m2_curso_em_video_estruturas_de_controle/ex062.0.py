a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
p = a1
z = 1
if z == 1:
    while a1 < (p + (r * 10)):
        print(a1,end=' ')
        a1 += r
    if a1 >= (p +(r * 10)):
        z = 2
        x = a1
elif z == 2:
    nova = int(input('Quer mostrar mais termos? Digite o número desejado. Digite 0 para encerrar o programa.'))
    if nova != 0:
        while a1 < (x +(r * nova)):
            a1 += r
            print(a1,end=' ')
    elif nova == 0:
        print('Fim do programa.')
