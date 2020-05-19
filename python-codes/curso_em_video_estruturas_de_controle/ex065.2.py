n = s = c = mai = men = 0
perg = 's'
while perg in 'sSSIMsim':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if men == 0:
        men = n
    if n > mai:
        mai = n
    if n < men:
        men = n
    perg = str(input('Quer continuar? [s/n] ')).strip()
m = s/c
print('Soma:',s,'\nQuant. números:',c,'\nMédia: {:.2f}'.format(m),'\nMaior:',mai,'\nMenor:',men)