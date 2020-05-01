nome=str(input('Qual é seu nome completo? ')).strip().upper().split()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))
#.split() adicionado pois aí não tem como um nome como 'silvana' dar true