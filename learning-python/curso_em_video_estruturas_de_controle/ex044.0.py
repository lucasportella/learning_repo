print('{:=^40}'.format('LOJAS PORTELLA'))
preço= float(input('Preço das compras: '))
forma= int(input('''FORMA DE PAGAMENTO:
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão

Digite o número da opção:
'''))
if forma == 1:
    print('O preço a pagar será de {:.2f}.'.format(preço * 0.9))
elif forma ==2:
    print('O preço a pagar será de {:.2f}.'.format(preço * 0.95))
elif forma ==3:
    print('Sua compra será parcelada em 2x de R${:.2F} sem juros.'.format(preço/2))
    print('O preço a pagar será de {:.2f}.'.format(preço))
elif forma ==4:
    parcela = int(input('Quantas parcelas: '))
    print('Sua compra será parcelada em {}x de R${:.2f} com juros de 20%.'.format(parcela,(preço+ preço*0.2)/parcela))
    print('O preço a pagar será de {:.2f}.'.format(preço+(preço * 0.2)))
else:
    print('Erro. Digite apenas 1,2,3 ou 4.')