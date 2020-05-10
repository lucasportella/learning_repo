somaid = 0
contmm = 0
contm2 = 0
conth = 0
maisvelho = 0

for c in range(1,5,1):
    nome = str(input('Nome da {}ª pessoa: '.format(c))).capitalize().strip()
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Sexo da {}ª pessoa(digite H para homem e M para mulher): '.format(c))).lower().strip()
    somaid += idade
    if sexo == 'm' and idade < 20:
        contmm += 1
    elif sexo == 'm':
        contm2 += 1
    elif sexo == 'h':
        conth += 1
        if maisvelho < idade:
            maisvelho = idade
            nomevelho = nome

media = somaid/4
print('A média de idade do grupo é: {:.1f} anos'.format(media))

if conth >=1:
    print('O homem mais velho se chama {}.'.format(nomevelho))

if contm2 == 0:
    print('Não há nenhuma mulher no grupo.')
elif contmm == 0 and contm2 > 0:
    print('Nenhuma mulher tem menos de 20 anos.')
elif contmm == 1:
    print('{} mulher tem menos de 20 anos.'.format(contmm))
elif contmm > 1:
    print('{} mulheres tem menos de 20 anos.'.format(contmm))

