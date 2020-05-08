n1=float(input('Digite curso_em_video_estruturas_de_controle primeira nota: '))
n2=float(input('Digite curso_em_video_estruturas_de_controle segunda nota: '))
media=float((n1+n2)/2)
print('A sua media foi de {}'.format(media))
if media >= 7:
    print('Você passou!')
else:
    print('Você reprovou!')