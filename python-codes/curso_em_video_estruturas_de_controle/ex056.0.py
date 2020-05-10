somaid= 0
contm = 0
for c in range(1,5,1):
    nome = str(input('Nome da {}ª pessoa: '.format(c))).capitalize().strip()
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Sexo da {}ª pessoa(digite H para homem e M para mulher): '.format(c))).lower().strip()
    somaid += idade
    if sexo == 'm' and idade < 20:
        contm += 1
    if c == 1 and sexo == 'h':
        maisvelho = idade
        nomevelho = nome
    elif c > 1 and sexo == 'h':
        if maisvelho < idade:
            maisvelho = idade
            nomevelho = nome


media = somaid/4
print('A média de idade do grupo é: {}'.format(media))

print('O homem mais velho se chama {}.'.format(nomevelho))
print('{} mulher(es) tem menos de 20 anos.'.format(contm))

