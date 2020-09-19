def ficha(jogador="<desconhecido>",gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

    
n = str(input("nome do Jogador: "))
g = str(input("Número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)