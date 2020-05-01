l=float(input('Diga a largura da sua parede em metros: '))
a=float(input('Diga a altura da sua parede em metros: '))
print('A área de sua parede tem {:.2f} m² e para pintá-la '.format(l*a),end=
'você precisará de {:.2f} litros de tinta.'.format((l*a)/2))
