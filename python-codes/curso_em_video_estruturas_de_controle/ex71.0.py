saque = int(input('Diga o valor do saque: '))
div50 = saque // 50
div50rest = saque % 50
print(
    f'Serão entregues:\n{div50} notas de R$50,00')
if div50rest >= 20:
    div20 = div50rest // 20
    div20rest = div50rest % 20
    print(f'{div20rest} notas de R$20,00')
    if div20rest >= 10:
        div10 = div20rest // 10
        div10rest = div20rest % 10
        print(f'{div10} notas de R$10,00')
        if div10rest >= 1:
            div1 = div10rest // 1
            div1rest = div10rest % 1
            print(f'{div1} notas de R$1,00')
elif div50rest >= 10:
        div10 = div50rest // 10
        div10rest = div50rest % 10
        if div10rest >= 1:
            div1 = div10rest // 1
            div1rest = div10rest % 1
elif div50rest >= 1:
    div1 = div50rest // 1
    div1rest = div50rest % 1

'''if div50rest >= 0.42 < 1:
    div20 = saque // 20
    div20rest = saque // 20
    print('a')'''