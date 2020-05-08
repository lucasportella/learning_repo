frase = str(input('Digite uma frase: ')).strip().lower().split()
junto = "".join(frase)
print(len(junto))
for c in range (len(junto),-1,-1):
    print(junto,end='')

'''if junto[c] == junto:
    print('Palíndromo')
else:
    print('Não é palíndromo')'''