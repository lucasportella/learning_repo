num=int(input('Digite um número inteiro: '))
base=int(input('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL
Sua opção(digite 1,2 ou 3): '''))
if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,(hex(num)[2]))) # botei um parenteses a mais nessa linha pois me pareceu sintaticamente mais correto
else:
    print('Você não digitou um número válido. Digite 1 2 ou 3 apenas.')