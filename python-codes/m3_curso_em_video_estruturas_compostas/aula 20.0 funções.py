def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    print(lista)

dobra([3,4,5])

def dobra(* lista):
    for c in lista:
        c *= 2
    print(lista)


dobra(3,4,5)
dobra(5,2,2,2,2,2,23,3,34)

