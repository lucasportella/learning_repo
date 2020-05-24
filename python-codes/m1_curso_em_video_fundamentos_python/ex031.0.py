dist=float(input('Qual a distância da sua viagem em km? '))
print('Você está prestes a começar uma viagem de {}Km'.format(dist))
#if dist > 200:
 #   print('O preço da sua passagem é R${:.2f}'.format(dist * 0.45))
#else:
 #   print('O preço da sua passagem é R${:.2f}'.format(dist * 0.50))
preço=dist * 0.50 if dist <= 200 else dist * 0.45
print('O preço da sua passagem é R${}'.format(preço))