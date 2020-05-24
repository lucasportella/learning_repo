valor1=float(input('Primeiro valor: '))
valor2=float(input('Segundo valor: '))
valor3=float(input('Terceiro valor: '))

if valor1 > valor2 and valor1 > valor3:
    print('O maior valor digitado foi {}'.format(valor1))
if valor2 > valor1 and valor2 > valor3:
    print('O maior valor digitado foi {}'.format(valor2))
if valor3 > valor1 and valor3 > valor2:
    print('O maior valor digitado foi {}'.format(valor3))

if valor1 < valor2 and valor1 < valor3:
    print('O menor valor digitado foi {}'.format(valor1))
if valor2 < valor1 and valor2 < valor3:
    print('O menor valor digitado foi {}'.format(valor2))
if valor3 < valor2 and valor3 < valor1:
    print('O menor valor digitado foi {}'.format(valor3))
