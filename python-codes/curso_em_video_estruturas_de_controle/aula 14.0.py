'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar[S/N]: '))

n = 1
impar = par = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
    else:
        impar += 1
print('Você digitou {} número(s) par(es) e {} número(s) ímpar(es).'.format(par,impar))'''

n = 1
impar = 0
par = -1 #super gambiarra
while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} número(s) par(es) e {} número(s) ímpar(es).'.format(par,impar))
