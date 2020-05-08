dist=float(input('Qual curso_em_video_estruturas_de_controle distância da sua viagem em km? '))
print('Você está prestes curso_em_video_estruturas_de_controle começar uma viagem de {}Km'.format(dist))
#if dist > 200:
 #   print('O preço da sua passagem é R${:.2f}'.format(dist * 0.45))
#else:
 #   print('O preço da sua passagem é R${:.2f}'.format(dist * 0.50))
preço=dist * 0.50 if dist <= 200 else dist * 0.45
print('O preço da sua passagem é R${}'.format(preço))