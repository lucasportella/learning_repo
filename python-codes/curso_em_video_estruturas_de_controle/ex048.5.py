sum = 0
num = 0
for c in range(1,501):
    if c % 2 != 0:
        if c % 3 == 0:
            sum += c # este é um acumulador
            num += 1 # este é um contador
print(sum,'é a soma')
print(num,'repetições')