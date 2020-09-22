cor = (
    '\033[m',         #fechar cor
    '\033[0;30;42m',  #verde
    '\033[0;30;44m',  #azul
    '\033[0;7;30m',   #branco(fundo)
    '\033[0;30;41m',   #vermelho
)


def ajuda(param):
    print(cor[3],end='')
    help(param)
    print(cor[0],end='')


def mensagem(texto, color=0):
    print(cor[color],end='')
    print('~' * (len(texto)+4))
    print(f'  {texto}')
    print('~' * (len(texto)+4))
    print(cor[0],end='')


while True:
    mensagem('SISTEMA DE AJUDA PyHELP', 1)
    comando = input('Função ou Biblioteca: ')
    if comando.upper() == 'FIM':
        mensagem('FIM',4)
        break
    else:
        mensagem("Acessando o manual do comando '{comando}'", 2)
        from time import sleep
        sleep(1)
        ajuda(comando)
