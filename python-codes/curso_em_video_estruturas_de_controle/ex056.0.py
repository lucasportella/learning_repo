somaid = 0
contm = 0
contm2 = 0
conth = 0

for c in range(1,5,1):
    nome = str(input('Nome da {}ª pessoa: '.format(c))).capitalize().strip()
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Sexo da {}ª pessoa(digite H para homem e M para mulher): '.format(c))).lower().strip()
    somaid += idade
    if sexo == 'm' and idade < 20:
        contm += 1
    elif sexo == 'm':
        contm2 += 1
    elif c == 1 and sexo == 'h':
        maisvelho = idade
        nomevelho = nome
        conth += 1
    elif c > 1 and sexo == 'h':
        if maisvelho < idade:
            maisvelho = idade
            nomevelho = nome
            conth += 1

media = somaid/4
print('A média de idade do grupo é: {:.1f} anos'.format(media))

if conth >=1:
    print('O homem mais velho se chama {}.'.format(nomevelho))

elif contm == 0 and contm2 > 0:
    print('Nenhuma mulher tem menos de 20 anos.')
elif contm == 1:
    print('{} mulher tem menos de 20 anos.'.format(contm))
elif contm > 1:
    print('{} mulheres tem menos de 20 anos.'.format(contm))

