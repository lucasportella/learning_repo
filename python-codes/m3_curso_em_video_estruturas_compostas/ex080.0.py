lista1 = []

num = int(input('Digite um número: '))
lista1.append(num)


num = int(input('Digite um número: '))
if num >= max(lista1):
    lista1.append(num)
elif num <= min(lista1):
    lista1.insert(0,num)


num = int(input('Digite um número: '))
if num >= max(lista1):
    lista1.append(num)
elif num <= min(lista1):
    lista1.insert(0,num)
else:
    lista1.insert(1,num)


num = int(input('Digite um número: '))
if num >= max(lista1):
    lista1.append(num)
elif num <= min(lista1):
    lista1.insert(0,num)
elif num >= lista1[1]:
    lista1.insert(2,num)
elif num <= lista1[1]:
    lista1.insert(1,num)


num = int(input('Digite um número: '))
if num >= max(lista1):
    lista1.append(num)
elif num <= min(lista1):
    lista1.insert(0,num)
elif num >= lista1[1]:
    lista1.insert(2,num)
elif num <= lista1[1]:
    lista1.insert(1,num)
elif num >= lista1[2]:
    lista1.insert(3,num)
elif num <= lista1[2]:
    lista1.insert(2,num)


print(lista1)