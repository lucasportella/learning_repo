lista1 = []
for c in range(5):
    lista1.append(int(input('Digite um número: ')))
maior = max(lista1)
menor = min(lista1)
lista1.sort()
maiorlist = []
menorlist = []
for pos, num in enumerate(lista1):
    if num == maior:
        maiorlist.append(pos)
    if num == menor:
        menorlist.append(pos)
print(f'O maior valor foi {maior} nas posições {maiorlist} e o '
      f'menor valor foi {menor} nas posições {menorlist}.')