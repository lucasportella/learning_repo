lista1 = []
valor = int()
lista1.append(int(input('Digite um valor: ')))
for c in range(0,4):
    valor = int(input('Digite um valor: '))
    if valor > max(lista1):
        lista1.append(valor)
    elif valor < min(lista1):
        lista1.insert(0,valor)
    else:
            for pos, n in enumerate(lista1):
                if valor >= n and valor <= lista1[pos+1]:
                    lista1.insert(pos+1,valor)
                    break
print(lista1)