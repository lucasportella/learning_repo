cores = {'padrão': '\033[m',
         'vermelho': '\033[31m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

from random import randint
from time import sleep

computador = randint(0, 5)
print('{}-=-'.format(cores['vermelho']) * 19)
print('{}Vou pensar num número... '.format(cores['padrão']))
print('{}-=-'.format(cores['vermelho']) * 19)
sleep(3)
jogador = int(input('{}Em qual número eu pensei? '.format(cores['padrão'])))
print('{}Processando...{}'.format(cores['amarelo'],cores['padrão']))
sleep(3)
if jogador == computador:
    print('{}Parabéns! Você ganhou!{}'.format(cores['azul'],cores['padrão']))
else:
    print('{}Eu ganhei! Eu pensei no número {} e não no {}!{}'.format(cores['pretoebranco'],computador, jogador,cores['padrão']))
