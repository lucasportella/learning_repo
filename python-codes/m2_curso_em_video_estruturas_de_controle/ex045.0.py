from time import sleep
from random import randint
opção=int(input('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual a sua jogada?
Digite 0,1 ou 2: '''))
opçãopc= randint(0,2)
print('-=' * 10)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if opção == 0:
    print('-='*15)
    print('Jogador escolheu Pedra')
    if opçãopc == 0:
        print('Computador escolheu Pedra')
        print('-=' * 15)
        print('EMPATE')
    elif opçãopc == 1:
        print('Computador escolheu Papel')
        print('-=' * 15)
        print('COMPUTADOR VENCE')
    elif opçãopc == 2:
        print('Computador escolheu Tesoura')
        print('-=' * 15)
        print('JOGADOR VENCE')
elif opção == 1:
    print('-=' * 15)
    print('Jogador escolheu Papel')
    if opçãopc == 0:
        print('Computador escolheu Pedra')
        print('-=' * 15)
        print('JOGADOR VENCE')
    elif opçãopc == 1:
        print('Computador escolheu Papel')
        print('-=' * 15)
        print('EMPATE')
    elif opçãopc == 2:
        print('Computador escolheu Tesoura')
        print('-=' * 15)
        print('COMPUTADOR VENCE')
elif opção == 2:
    print('-=' * 15)
    print('Jogador escolheu Tesoura')
    if opçãopc == 0:
        print('Computador escolheu Pedra')
        print('-=' * 15)
        print('COMPUTADOR VENCE')
    elif opçãopc == 1:
        print('Computador escolheu Papel')
        print('-=' * 15)
        print('JOGADOR VENCE')
    elif opçãopc == 2:
        print('Computador escolheu Tesoura')
        print('-=' * 15)
        print('EMPATE')
else:
    print('Erro, digite apenas 0, 1 ou 2.')
