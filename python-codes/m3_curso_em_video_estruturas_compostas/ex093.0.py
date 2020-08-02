dicio = {}
dicio["Nome"] = str(input('Nome do jogador: '))
dicio["Partidas"] = int(input(f'Quantas partidas {dicio["Nome"]} jogou? '))
lista = []
for c in range(dicio["Partidas"]):
    dicio["Gols"] = int((input(f'Quantos gols na partida {c+1}: ')))
    lista.append(dicio["Gols"])
dicio["Gols"] = lista
total = int()
for c in lista:
    total += c
dicio["Total"] = total
print('-='*30)
print(dicio)
print('-='*30)
for c, v in dicio.items():
    if c != 'Partidas':
        print(f'O campo {c} tem o valor {v}')
print('-='*30)
print(f'O jogador {dicio["Nome"]} jogou {dicio["Partidas"]} partidas.')
for c, v in enumerate(lista):
    print(f'   => Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {total} gols.')