from math import sqrt
catetoposto=float(input('Digite o valor do cateto oposto: '))
catetadjacente=float(input('Digite o valor do cateto adjacente '))
hipotenusa=sqrt(pow(catetadjacente,2)+pow(catetoposto,2))
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))