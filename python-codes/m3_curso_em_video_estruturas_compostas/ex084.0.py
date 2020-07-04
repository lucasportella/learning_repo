#variaveis
lista = []
sublista = []
cadastro = int()
maiorpeso = float()
menorpeso = float ()
maiorlista = []
menorlista = []
maiorpesoind = float()
menorpesoind = float()


while True:

    #listacompleta
    continuar = 'z'
    nome = str(input('Nome: '))
    sublista.append(nome)
    cadastro += 1
    peso = float(input('Peso: '))
    sublista.append(peso)

    #maiorpeso
    if peso > maiorpesoind:
        maiorlista.clear()
        maiorpesoind = peso
    if peso == maiorpesoind:
        maiorlista.append(nome)

    #menorpeso
    if cadastro == 1:
        menorpesoind = peso
        menorlista.append(nome)
    else:
        if peso < menorpesoind:
            menorlista.clear()
            menorpesoind = peso
        if peso == menorpesoind:
            menorlista.append(nome)

    #lista completa
    lista.append(sublista[:])
    sublista.clear()

    #continuar
    while continuar not in 'S' or continuar not in 'N':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
        if continuar in 'N':
            break
        if continuar in 'S':
            break
    if continuar in 'N':
        break

#resultado
print('-='*30)
print(f'Todos: {lista}')
print(f'Ao todo, você cadastrou {cadastro} pessoas.')
print(f'O maior peso foi de {maiorpesoind} Kg. Peso de {maiorlista}')
print(f'O menor peso foi de {menorpesoind} Kg. Peso de {menorlista}')