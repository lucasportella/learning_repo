from time import sleep
from random import randint
lista = []
num_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-=- Sorteando {num_jogos} jogos =-=-=-')
for c in range(num_jogos):
    for d in range(6):
        lista.append(randint(0,60))
    sleep(1)
    print(f'Jogo {c+1}: {lista}')
    lista.clear()
