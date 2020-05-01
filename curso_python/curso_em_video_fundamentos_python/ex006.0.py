n=int(input('Digte um número para saber o seu dobro, triplo e sua raiz quadrada: '))
print('O dobro é {}, o triplo é {} e sua raiz quadrada é {:.99f}'.format(n*2,n*3,n**(1/2)))

nx=float(input('Digite um número: '))
d=nx*2
t=nx*3
r=nx**(1/2)
print('O dobro de {} é {}.'.format(nx,d))
print('O triplo de {} é {}.'.format(nx,t))
print('A raiz quadrada de {} é {}'.format(nx,r))