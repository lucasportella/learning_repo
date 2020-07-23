from time import sleep
from random import sample
lista = []
num_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-=- Sorteando {num_jogos} jogos =-=-=-')
for c in range(num_jogos):
    lista = sample(range(60), 6)
    lista.sort()
    sleep(1)
    print(f'Jogo {c+1}: {lista}')
    lista.clear()
