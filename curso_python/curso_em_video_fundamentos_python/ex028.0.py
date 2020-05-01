import random
num=int(random.randrange(0,5))
guess=int(input('Qual o número que pensei? '))
if guess == num:
    print('Parabéns! Voce acertou!')
else:
    print('Você errou! O número que tinha pensado era {}'.format(num))
