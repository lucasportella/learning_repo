def ajuda():
    while True:
        print('\033[0;30;42m~' * 30)
        print('SISTEMA DE AJUDA PyHELP')
        print('~' * 30)
        print('\033[m', end='')

        escolha = input('Função ou biblioteca: ')
        if escolha == "fim":
            print('\033[0;30;41m~' * 30)
            print('FIM')
            print('~' * 30)
            print('\033[m')
            break

        print('\033[0;30;44m~' * 30)
        print(f"Acessando o manual do comando '{escolha}'")
        print('~' * 30)
        print('\033[m', end='')
        from time import sleep
        sleep(1)
        print('\033[7;30m')
        print(help(escolha))
        print('\033[m', end='')


print(ajuda())
