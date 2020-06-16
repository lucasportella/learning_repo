lista = list()
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n >= lista[-1]:
        lista.append(n)
    elif n <= lista[0]:
        lista.insert(0,n)
    else:
        pos = 0
        while n > lista[pos]:
            pos += 1
            if lista[pos] > n:
                lista.insert(pos,n)
                break
print(lista)

