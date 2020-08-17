def calculo(largura, comprimento):
    multiplicacao = largura * comprimento
    print(f'A área de um terreno {largura:.2f} x {comprimento:.2f} é de {multiplicacao:.2f}m².')


print('Controle de Terrenos')
print('='*20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
calculo(largura=larg, comprimento=comp)
