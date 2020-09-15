def ficha(nome=0,gols=0):
    print('-'*20)
    if len(nome) < 1:
        nome = "desconhecido"

    if type(gols) is str:
        gols = 0
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


ficha(str(input("Nome do jogador: ")),(input("Número de gols: ")))
