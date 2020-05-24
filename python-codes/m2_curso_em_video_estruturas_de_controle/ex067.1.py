while True:
    tab = int(input('Digite um número: '))
    if tab < 0:
        break
    for c in range(1,11):
        print(f'{tab} x {c} = {tab * c}')
    print('-'*30)