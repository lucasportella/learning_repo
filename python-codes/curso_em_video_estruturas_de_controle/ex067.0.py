c = 1
while True:
    while c < 11:
        if c == 1:
            tab = int(input('Quer ver a tabuada de qual valor? '))
        if tab < 0:
            break
            print('-' *40)
        print(f'{tab} x {c} = {tab * c}')
        c +=1
        if c > 10:
            c = 1
    if tab < 0:
        break