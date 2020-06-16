lista1 = []
while True:
    cont = 'R'
    lista1.append(int(input('Digite um número: ')))
    while cont not in 'SSIMNNÃONAO':
        cont = str(input('Deseja continuar: ')).strip().upper()
    if cont in 'NNÃONAO':
        break
print(f'{len(lista1)} números foram digitados.')
lista1.sort(reverse=True)
print(lista1)
if 5 in lista1:
    print('O valor 5 está na lista.')

