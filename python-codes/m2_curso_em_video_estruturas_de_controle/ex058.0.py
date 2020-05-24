import random
n = int(random.randint(0,1))
c = 1
guess = int(input('Que número pensei? (0-10) '))
while guess != n:
    if guess < n:
        print('Errou. É maior...')
    elif guess > n:
        print('Errou. É menor...')
    c += 1
    guess = int(input('Que número pensei? (0-10) '))

print('Voce acertou com {} tentativa(s).'.format(c))