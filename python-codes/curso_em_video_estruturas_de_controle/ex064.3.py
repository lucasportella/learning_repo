n = c = soma = 0
n = int(input('Digite um número [999 /p parar]: '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número [999 /p parar]: '))
print('Soma: {}\nTotal de números: {}'.format(soma,c))