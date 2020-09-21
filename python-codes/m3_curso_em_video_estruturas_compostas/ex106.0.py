from time import sleep
def ajuda(a=0):
    print('\033[0;30;42m~'*30)
    print('SISTEMA DE AJUDA PyHELP')
    print('~'*30)

    a = input('\033[mFunção ou Biblioteca: ')

    print('\033[0;30;44m~'*30)
    print(f"Acessando o manual do comando '{a}'")
    print('~'*30)
    print('\033[m')
    sleep(1)


print(f'\033[7;30m{ajuda()}')
