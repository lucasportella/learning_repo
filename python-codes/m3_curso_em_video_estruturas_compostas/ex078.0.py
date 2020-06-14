lista1 = []
for c in range(0,5):
    lista1.append(int(input(f'Digite o {c+1}º número: ')))
maxlist = [max(lista1)+1,]
minlist = [min(lista1)+1,]
maior = []
menor = []
for pos, e in enumerate(lista1):
    if e == max(lista1):
        maior.append(pos)
    if e == min(lista1):
        menor.append(pos)
print(f'O maior número foi {max(lista1)} e sua posição na lista é {maior}.')
print(f'O menor número foi {min(lista1)} e sua posição na lista é {menor}.')