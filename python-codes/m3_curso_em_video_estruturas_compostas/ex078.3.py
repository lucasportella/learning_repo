lista1 = []
for c in range(5):
    lista1.append(int(input('Digite um número: ')))
lista1.sort()
maior = max(lista1)
menor = min(lista1)
print('-'*30)
print(f'Os maiores valores digitados foram:')
for pos, num in enumerate(lista1):
    if num == maior:
        print(f'O número {num}, na posição {pos}.')
print('-'*30)
print(f'Os menores valores digitados foram:')
for pos, num in enumerate(lista1):
    if num == menor:
        print(f'O número {num}, na posiçõa {pos}.')