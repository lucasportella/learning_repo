lista = [[],[]]
for c in range(1,8):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(sorted(lista[0]))
print(sorted(lista[1]))
#da pra fazer tbm lista[0].sort() e lista[1].sort()