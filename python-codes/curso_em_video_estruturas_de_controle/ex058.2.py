from random import randint
computador = randint(0,10)
print('Pensei num número de 0 a 10. Adivinhe.')
acertou = False
palpites = 0
print(computador)
while acertou == False:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Você acertou com {} tentativa(s)'.format(palpites))