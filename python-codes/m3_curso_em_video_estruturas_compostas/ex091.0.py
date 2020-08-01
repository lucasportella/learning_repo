from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
print('Valores sorteados:')
for c,v in jogo.items():
    print(f'O {c} tirou {v}.')
    sleep(0.5)
ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1),reverse=True)
print('-'*50)
for c, v in enumerate(ranking):
    print(f'{c+1}º Lugar foi do {v[0]} que tirou {v[1]}.')
