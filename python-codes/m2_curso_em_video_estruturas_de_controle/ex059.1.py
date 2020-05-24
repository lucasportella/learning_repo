from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
menu = 0
while menu != 5:
    menu = int(input('''=-==-==-==-==-==-==-==-==-==-=
    [1] Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do Programa
    >>>>> Qual é a sua opção? '''))
    if menu == 1:
        print('A soma entre {} e {} é {}.'.format(n1,n2,n1+n2))
        sleep(2)
    elif menu == 2:
        print('A multiplicação entre {} e {} é {}.'.format(n1,n2,n1*n2))
        sleep(2)
    elif menu == 3:
        print('O maior número é {}.'.format(max(n1,n2)))
        sleep(2)
    elif menu == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa.')