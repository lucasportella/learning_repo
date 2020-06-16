lista1 = []
while True:
    cont = ''
    lista1.append(int(input('Digite um número: ')))
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while cont not in 'SSIMNNÃONAO':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cont in 'NNÃONAO':
        break
listapar = []
listaimpar = []
for n in lista1:
    if n % 2 == 0:
        listapar.append(n)
    elif n % 2 != 0:
        listaimpar.append(n)
print(lista1)
print(listapar)
print(listaimpar)