frase = str(input('Digite uma frase: ')).lower()
frase = ''.join(frase.split())
ordem = (frase[0:])
invert = (frase[::-1])
print('O inverso de {} é {}.'.format(ordem,invert))
if ordem == invert:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo.')