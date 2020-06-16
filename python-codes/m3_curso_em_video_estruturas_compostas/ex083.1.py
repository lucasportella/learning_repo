lista1 = []
lista2 = []
exp = str(input('Digite a expressão: '))
for c in exp:
    if c == '(':
        lista1.append('(')
    if c == ')':
        lista2.append(')')
if exp[0] == ')' or exp[-1] =='(':
    print('Sua expressão está errada!')
else:
    if len(lista1) == len(lista2):
        print('Sua expressão está correta!')
    else:
        print('Sua expressão está errada!')