while True:
    cont = ' '
    tupla = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis',
         'Sete','Oito','Nove','Dez','Onze','Doze','Treze',
         'Quatorze','Quinze','Dezesseis','Dezessete',
         'Dezoito','Dezenove','Vinte')
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {tupla[num]}.')
    while cont not in 'SSIMNNÃONAO':
        cont = str(input('Deseja continuar? [S/N] ').upper())
    if cont in'NNÃONAO':
        break