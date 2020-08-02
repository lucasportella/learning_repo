dicio = {}
dicio["Nome"] = str(input('Nome do jogador: '))
dicio["Partidas"] = int(input(f'Quantas partidas {dicio["Nome"]} jogou? '))
for c in range(dicio["Partidas"]):
    dicio["Gols"] = int((input(f'Quantos gols na partida {c+1}: ')))
print(dicio)