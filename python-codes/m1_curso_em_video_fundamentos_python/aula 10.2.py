n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=float((n1+n2)/2)
print('A sua media foi de {}'.format(media))
if media >= 7:
    print('Você passou!')
else:
    print('Você reprovou!')