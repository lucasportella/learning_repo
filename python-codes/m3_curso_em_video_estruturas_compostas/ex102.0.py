def fatorial(número, show=0):
    resultado = 1

    if show == True:

        if número == 0:
            print("0! = 1",end='')

        if número == 1:
            print("1! = 1")

        else:
            print(f"{número}! = ", end='')
            for c in range(número,0,-1):
                resultado *= c
                if c > 1:
                    print(f"{c} x ", end="")
                else:
                    print(f"{c} = {resultado}")

    elif show == False:
        print(f"{número}! = ", end='')
        for c in range(número, 0, -1):
            resultado *= c
        print(resultado)


fatorial(int(input("Número para fatorial: ")),show=False)
