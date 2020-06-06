numeros = tuple(int(input(f'Digite o {i+1}º número: '))for i in range(4))
print(type(numeros))
print(numeros)
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'Posição do primeiro 3 digitado: {numeros.index(3)+1}')
else:
    print('Nenhum 3 foi digitado.')
cont = tuple()
for c in numeros:
    if c % 2 == 0:
        cont += c,
if cont == ():
    print('Nenhum par digitado.')
else:
    print(f'Números pares digitados: {cont}')