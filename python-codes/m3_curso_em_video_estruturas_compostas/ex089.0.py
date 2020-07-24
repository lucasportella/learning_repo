lista =[]
lista2 = []
continuar = ' '
contador = 0
while True:
    lista.append(input('Digite o nome do aluno: '))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))

    media = (lista[1] + lista[2])/2
    lista2.append([lista[0],media])
    lista.clear()
    while continuar not in 'S' or continuar not in 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continuar in 'N':
            break
        if continuar in 'S':
            break
    if continuar in 'N':
        break
print('-='*30)
print(f'No. NOME:             MÉDIA:')
print('-'*30)
while contador < len(lista2):
    print(f'{contador}   {lista2[contador][0]:<18}{lista2[contador][1]:.2f}')
    contador += 1