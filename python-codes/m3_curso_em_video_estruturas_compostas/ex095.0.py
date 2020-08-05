jogadores = []
continuar = ' '
while True:
    dicio = {"Nome": str(input('Nome do jogador: '))}
    partidas = int(input(f'Quantas partidas {dicio["Nome"]} jogou? '))
    sublista_gols = []
    for c in range(partidas):
        dicio["Gols"] = int((input(f'Quantos gols na partida {c+1}: ')))
        sublista_gols.append(dicio["Gols"])
    jogadores.append(dicio.copy())
    dicio["Gols"] = sublista_gols
    print('-'*40)
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        if continuar == 'S':
            break
        elif continuar == 'N':
            break
    if continuar == 'N':
        break

total = int()
for c in sublista_gols:
    total += c
dicio["Total"] = total
print('-='*30)
print(jogadores)
print('-='*30)
for c, v in dicio.items():
    print(f'O campo {c} tem o valor {v}')
print('-='*30)
print(f'O jogador {dicio["Nome"]} jogou {partidas} partidas.')
for c, v in enumerate(sublista_gols):
    print(f'   => Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {total} gols.')
