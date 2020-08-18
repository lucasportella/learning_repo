from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if fim >= inicio:
        for c in range(inicio,fim+1,passo):
            #sleep(0.3)
            print(c,end=' ')
    elif fim < inicio:
        if passo > 0:
            passo = -passo
        for c in range(inicio,fim-1,passo):
            #sleep(0.3)
            print(c,end=' ')

    print('FIM!')
    print('-='*20)


contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)
print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
