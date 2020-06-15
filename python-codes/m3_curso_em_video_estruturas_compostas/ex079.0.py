lista1 = []
cont = 'S'
valor = int()
while True:
    if cont in 'S,SIM':
        valor = int(input('Digite um valor: '))
        if valor not in lista1:
            lista1.append(valor)
            print('Valor adicionado com sucesso...')
        elif valor in lista1:
            print('Valor duplicado! Não vou adicionar...')
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    elif cont in 'N,NÃO,NAO':
        break
    else:
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
lista1.sort()
print(f'Valores digitados em ordem: {lista1}')