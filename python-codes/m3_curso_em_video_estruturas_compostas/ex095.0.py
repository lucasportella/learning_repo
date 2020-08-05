jogadores = []
continuar = ' '
while True:
    dicio = {"Nome": str(input('Nome do jogador: '))}
    partidas = int(input(f'Quantas partidas {dicio["Nome"]} jogou? '))
    sublista_gols = []
    for c in range(partidas):
        dicio["Gols"] = int((input(f'Quantos gols na partida {c+1}: ')))
        sublista_gols.append(dicio["Gols"])
        dicio["Gols"] = sublista_gols
        total = int()
        for c in sublista_gols:
            total += c
        dicio["Total"] = total
    jogadores.append(dicio.copy())

    print('-'*40)
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        if continuar == 'S':
            break
        elif continuar == 'N':
            break
    if continuar == 'N':
        break

print('-='*30)
print(jogadores)
print(dicio)
print('-='*30)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total"}')
