a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termos = int(input('Quantidade de termos: '))
p = a1
z = 1

while z == 1:
    if a1 < (p +(r * termos)):
        print(a1,'->',end=' ')
        a1 += r
    elif a1 >= (p +(r * 10)):
        print('Fim')
        z = 2
        x = a1
        question = int(input('\nMais termos? Diga quantos. Diga 0 para encerrar o programa. '))
        if question != 0:
            z = 1
        elif a1 < (x + (x * question)):
            a1 += r
            print(a1,end=' ')
        elif a1 >= (x + (x * question)):
            print('Fim')
            z = 1
