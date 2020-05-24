n = s = c = mai = men = 0
n = int(input('Digite um número [999 p/ parar]: '))
while n != 999:
    c += 1
    s += n
    if n > mai:
        mai = n
    if n < men:
        men = n
    n = int(input('Digite um número [999 p/ parar]: '))
if s == 0 and c == 0:
    m = 'indeterminado'
    print('Soma:', s, '\nQuant. números:', c, '\nMédia:',m, '\nMaior:', mai, '\nMenor:', men)
else:
    m = s/c
    print('Soma:',s,'\nQuant. números:',c,'\nMédia: {:.1f}'.format(m),'\nMaior:',mai,'\nMenor:',men)