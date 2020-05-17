n = c = s = 0
n = int(input('Digite um número [999 p/ parar]: '))
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um número [999 p/ parar]: '))
m = s/c
print('Soma:',s,'\nQuant. números:',c,'\nMédia:',m)