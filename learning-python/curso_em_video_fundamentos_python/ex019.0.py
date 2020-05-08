import random
a1=input('Primeiro Aluno: ')
a2=input('Segundo Aluno: ')
a3=input('Terceiro Aluno: ')
a4=input('Quarto Aluno: ')
lista = [a1,a2,a3,a4]
#print('O aluno escolhido foi {}'.format(random.choice(lista)))
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))