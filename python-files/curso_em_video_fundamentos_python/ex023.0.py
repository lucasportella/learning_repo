n=int(input('Informe um número: '))
un=n//1 % 10
de=n//10 % 10
ce=n//100 % 10
mi=n//1000
print('Analisando o número {}'.format(n))
print('Unidade: {}'.format(un))
print('Dezena: {}'.format(de))
print('Centena: {}'.format(ce))
print('Milhar: {}'.format(mi))