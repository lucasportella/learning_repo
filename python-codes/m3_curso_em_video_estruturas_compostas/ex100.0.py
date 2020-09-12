from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista:',end=' ')
    for c in range(5):
        sleep(0.3)
        numeros.append(randint(0,10))
        print(numeros[c],end=' ')
    print('PRONTO!')

def soma():
    paressoma = int()
    for d in numeros:
        if d % 2 == 0:
            paressoma += d
    print(f'Somando os valores pares de {numeros}, temos {paressoma}')


numeros = []

sorteia()
soma()
