flag = 0
soma = 0
c = 0
while flag != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        flag = 999
        soma -= 999
        c -= 1
    soma += n
    c += 1
print('Quantidade de números digitados: {}\nSoma: {}'.format(c,soma))