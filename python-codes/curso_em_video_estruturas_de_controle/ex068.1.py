from random import randint
v = 0
while True:
    pc = int(randint(0,10))
    num = int(input('Digite um número: '))
    soma = pc + num
    escolha = ' '
    while escolha not in 'IP':
        escolha = str(input('Par ou ímpar?[P/I] ')).upper().strip()[0]
        if escolha == 'P':
            if soma % 2 == 0:
                v += 1
                print(f'{num} + {pc} é = {soma}, que dá PAR!')
                print('Você ganhou!')
                print('Vamos jogar de novo...')
                print('=-' * 15)
            elif soma % 2 != 0:
                print(f'{num} + {pc} é = {soma}, que dá ÍMPAR!')
                print('Você perdeu!')


        if escolha == 'I':
            if soma % 2 != 0:
                v += 1
                print(f'{num} + {pc} é = {soma}, que dá ÍMPAR!')
                print('Você ganhou!')
                print('Vamos jogar de novo...')
                print('=-' * 15)
            elif soma % 2 == 0:
                print(f'{num} + {pc} é = {soma}, que dá PAR!')
                print('Você perdeu!')

    if soma % 2 == 0 and escolha in'I':
        break
    elif soma % 2 != 0 and escolha in 'P':
        break

print(f'GAME OVER! Seu total de vitórias foi {v}.')


