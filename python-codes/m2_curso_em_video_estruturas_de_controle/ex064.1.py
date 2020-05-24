flag = soma = c = 0
while flag != 999:
    n = int(input('Digite um número [999 p/ parar]: '))
    if n == 999:
        flag = 999
        print('Quantidade de números digitados: {}\nSoma: {}'.format(c, soma))
    soma += n
    c += 1