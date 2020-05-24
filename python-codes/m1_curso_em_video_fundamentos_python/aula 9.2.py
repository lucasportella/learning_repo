frase='Curso em Vídeo Python'
frase=frase.replace('Pyhon','Android')
print(frase)
print('Curso' in frase)
print(frase.find('rso'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
dividido=frase.split()
print(dividido[3][3])