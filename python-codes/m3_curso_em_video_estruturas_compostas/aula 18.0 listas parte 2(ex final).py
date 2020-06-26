lista1 = []
sublista1 = []
maior = menor = 0

for c in range(3):
    sublista1.append(str(input('Digite seu nome: ')))
    sublista1.append(int(input('Qual a sua idade: ')))
    if sublista1[1] > 18:
        maior += 1
    else:
        menor += 1
    lista1.append(sublista1[:])
    sublista1.clear()

for c in lista1:
    if c[1] >= 18:
        print(f'{c[0]} é maior de idade.')
    else:
        print(f'{c[0]} é menor de idade.')

print(f'Maiores de idade: {maior} pessoas.')
print(f'Menores de idade: {menor} pessoas.')