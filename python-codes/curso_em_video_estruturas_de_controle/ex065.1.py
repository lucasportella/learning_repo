n = s = c = mai = men = 0
n = int(input('Digite um número [999 p/ parar]: '))
men = n
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
else:
    m = s/c
print('Soma:',s,'\nQuant. números:',c,'\nMédia:',m,'\nMaior:',mai,'\nMenor:',men)