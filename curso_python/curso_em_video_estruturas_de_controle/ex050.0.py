soma = 0
cont = 0
for b in range(1,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('soma:',soma)
print('contador de pares:',cont)