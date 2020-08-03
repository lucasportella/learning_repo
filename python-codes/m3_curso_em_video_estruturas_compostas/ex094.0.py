lista = []
dicio = {}
dicio["Sexo"] = ""
continuar = ' '
while True:
    dicio["Nome"] = (input('Nome: '))
    lista.append(dicio["Nome"])
    while True:
        if dicio["Sexo"] != 'M' or 'F':
            dicio["Sexo"] = str(input('Sexo: [M/F] ')).upper().strip()
        if dicio["Sexo"] == 'M' or dicio["Sexo"] == 'F':
            lista.append(dicio["Sexo"])
            break


    dicio["Idade"] = int(input('Idade: '))

    while continuar not in 'S' or continuar not in 'N':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
        if continuar in 'N':
            break
        if continuar in 'S':
            break
    if continuar in 'N':
        break