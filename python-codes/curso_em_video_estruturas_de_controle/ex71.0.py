saque = int(input('Diga o valor do saque: '))
div50 = saque // 50
div50rest = saque % 50
if div50rest > 0:
    div20rest = div50rest // 20
    if div20rest > 0:
        div10rest = div20rest // 10
    else:
        div10rest = div50rest // 10
        if div10rest > 0:
            div1rest = div10rest // 1
        else: div1 = div10rest // 1
