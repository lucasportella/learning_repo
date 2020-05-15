a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
p = a1
z = 0
while a1 < (p + p * 10) and z == 0:
    print(a1,'->',end=' ')
    a1 += r
x = a1
if a1 >= (p + p * 10):
    print('Fim')
    question = int(input('\nQuer mostrar mais termos? Digite 0 para encerrar o programa. '))
    if question == 0:
        print('Fim do programa.')
    else:
        while a1 < x + r * question:
            a1 += r
            print(a1,'->',end=' ')
