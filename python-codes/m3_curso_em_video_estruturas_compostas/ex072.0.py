while True:
    t = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
    n = int(input('Digite um número entre 0 e 20: '))
    p = ' '
    while n < 0 or n >20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {t[n]}.')
    while p not in 'SSIMNNÃONAO':
        p = str(input('Deseja continuar? [S/N] ')).upper()
    if p in 'SSIM':
        p = ' '
    elif p in 'NNÃONAO':
        break
