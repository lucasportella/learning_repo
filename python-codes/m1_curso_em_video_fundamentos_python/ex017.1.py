from math import hypot
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))
hipo=hypot(co,ca)
#print('A hipotenusa é {:.2f}'.format(hipo))
print(f'A hipotenusa é {hipo}')