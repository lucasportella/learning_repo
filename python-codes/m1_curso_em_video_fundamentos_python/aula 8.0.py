import math
num=int(input('Digite um número: '))
raiz=math.sqrt(num)
raizfloor=math.floor(raiz)
#raiz=num**(1/2)
#print('A raiz de {} é igual a {}'.format(num,math.ceil(raiz)))
#print('A raiz de {} é igual a {}'.format(num,math.floor(raiz)))
print('A raiz de {} é igual a {}'.format(num,raizfloor))
