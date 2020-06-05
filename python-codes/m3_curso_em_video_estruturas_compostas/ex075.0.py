val = tuple('')
for x in range(0,4):
    val += tuple(input('Digite um valor: '))
print(f'O valor 9 apareceu {val.count("9")} vezes')
val = str(val)
print(val)
print(f'A posição do primeiro 3 foi {val.find("3")}')
