from time import sleep


def maior(*numeros):
    maior_numero = int()
    print('=-' * 30)
    print('Analisando os valores passados...')
    for c in numeros:
        if c > maior_numero:
            maior_numero = c
        sleep(0.3)
        print(c, end=' ')
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {maior_numero}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()
