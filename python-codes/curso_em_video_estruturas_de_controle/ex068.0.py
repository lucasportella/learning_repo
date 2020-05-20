from random import randint
print('=-'* 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'* 15)
v = 0

while True:
    pc = randint(0,10)
    valor = int(input('Digite um valor: '))

    if (valor + pc) % 2 == 0:
        resultadosoma = 'PAR'
    else: resultadosoma = 'ÍMPAR'


    escolha = str(input('Par ou ímpar? [P/I] ')).upper().strip()
    print('-' * 30)
    print(f'Você jogou {valor} e o computador jogou {pc}. Total de {valor + pc} deu {resultadosoma}')
    print('-' * 30)


    if escolha in 'PPAR':
        if (valor + pc) % 2 == 0:
            print('Você GANHOU!!')
            print('Vamos jogar novamente...')
            print('=-' * 15)
            v += 1
        else:
            print('Voce PERDEU!!')
            print('-=' * 15)
            print(f'GAME OVER! Você venceu {v} vez(es).')
            break


    elif escolha in 'ÍIMPARÍMPAR':
        if (valor + pc) % 2 != 0:
            print('Você GANHOU!!')
            print('Vamos jogar novamente...')
            print('=-' * 15)
            v += 1
        else:
            print('Você PERDEU!!')
            print('-=' * 15)
            print(f'GAME OVER! Você venceu {v} vez(es).')
            break
