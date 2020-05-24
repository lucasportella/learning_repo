n = c = soma = 0
while n != 999:
    n = int(input('Digite um número [999 /p parar]: '))
    if n != 999:
        soma += n
        c += 1
print('Soma: {}\nTotal de números: {}'.format(soma,c))
