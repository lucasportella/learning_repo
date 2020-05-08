dias=int(input('Quantos dias alugados? '))
km=float(input('Quantos Km rodados? '))
diascalculo=dias*60
kmcalculo=km*0.15
total=diascalculo+kmcalculo
print('O total curso_em_video_estruturas_de_controle pagar é de R${:.2f}'.format(total))