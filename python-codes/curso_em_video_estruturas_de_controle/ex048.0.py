soma = 0
somaPA = 0
print('Todos os números ímpares múltiplos de 3 até 500:')
for cont in range(1,501,2):
    if cont % 3 == 0:
        soma += 1
        somaPA += cont
        print(cont,end=' ')
print('\n Número de repetições:', soma)
print('Soma da PA:', somaPA)
