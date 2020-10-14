from time import sleep
from ex115 import modulos
flag = False
while flag == False:
    print('-'*60)
    print(f'{"MENU PRINCIPAL":^60}')
    print('-'*60)
    print(f'{modulos.colorizar("1","amarelo")}- Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-'*60)
    try:
        opção = int(input('Sua opção: '))
        opção > 0
    except (TypeError, ValueError):
        print('ERRO: Digite um número inteiro válido!')
        continue
    else:
         if opção < 1 or opção > 3:
             print('ERRO: Número digitado fora do interválo!')
             continue
         elif opção == 1:
             print('-' * 60)
             print(f'{f"Opção {opção}":^60}')
             print('-' * 60)
             sleep(2)
         elif opção == 2:
             print('-' * 60)
             print(f'{f"Opção {opção}":^60}')
             print('-' * 60)
             sleep(2)
         elif opção == 3:
             print('-' * 60)
             print(f'{f"Opção {opção}":^60}')
             print('-' * 60)
             sleep(2)
             print(f'{"Saindo do sistema... Até logo!":^60}')
             print('-' * 60)
             break