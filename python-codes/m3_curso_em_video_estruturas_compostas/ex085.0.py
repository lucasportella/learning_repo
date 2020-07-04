lista = []
listapar = []
listaimpar = []
for c in range(7):
    lista.append(int(input('Digite um valor: ')))
lista.sort()
print(lista)
for c in lista:
        if c % 2 == 0:
            listapar.append(c)
        else:
            listaimpar.append(c)
listapar.sort()
listaimpar.sort()
print(listapar)
print(listaimpar)

