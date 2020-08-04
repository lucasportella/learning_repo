lista = []
dicio = {}
dicio["Nome"] = ""
dicio["Sexo"] = ""
dicio["Idade"] = ""
continuar = ' '

while True:
    dicio["Nome"] = (input('Nome: '))
    lista.append(dicio["Nome"])
    while True:
        dicio["Sexo"] = str(input('Sexo: [M/F] ')).upper().strip()
        if dicio["Sexo"] == 'M' or dicio["Sexo"] == 'F':
            lista.append(dicio["Sexo"])
            break
        if dicio["Sexo"] not in 'M' or 'F':
            print('Erro! Por favor, digite apenas M ou F')



    dicio["Idade"] = int(input('Idade: '))

    while continuar not in 'S' or continuar not in 'N':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
        if continuar in 'N':
            break
        elif continuar in 'S':
            break
        else:
            print('Erro! Responda apenas S ou N.')
    if continuar in 'N':
        break
print('-='*30)
print(lista)
print(dicio)
print(f'Ao todo temos {len(dicio["Nome"])} pessoas cadastradas.')