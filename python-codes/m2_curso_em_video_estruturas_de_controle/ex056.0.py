somaid = 0
contmm = 0
contm2 = 0
conth = 0
maisvelho = 0
nomevelho = ''

for c in range(1,5,1):
    print(' -----{}ª PESSOA -----'.format(c))
    nome = str(input('Nome da {}ª pessoa: '.format(c))).capitalize().strip()
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Sexo da {}ª pessoa [M/F]: '.format(c))).lower().strip()
    somaid += idade
    if sexo == 'f' and idade < 20:
        contmm += 1
        contm2 += 1
    elif sexo == 'f':
        contm2 += 1

    elif sexo == 'm':
        conth += 1
        if idade >= maisvelho:
            maisvelho = idade
            nomevelho = nome
        else:
            print('Erro, idade não pode ser menor que zero.')

media = somaid/4
print('A média de idade do grupo é: {:.1f} anos'.format(media))

if conth >=1:
    print('O homem mais velho se chama {} e ele tem {} ano(s).'.format(nomevelho,maisvelho))
elif conth == 0:
    print('Não há nenhum homem no grupo.')


if contm2 == 0:
    print('Não há nenhuma mulher no grupo.')
elif contmm == 0 and contm2 > 0:
    print('Nenhuma mulher tem menos de 20 anos.')
elif contmm == 1:
    print('{} mulher tem menos de 20 anos.'.format(contmm))
elif contmm > 1:
    print('{} mulheres tem menos de 20 anos.'.format(contmm))

