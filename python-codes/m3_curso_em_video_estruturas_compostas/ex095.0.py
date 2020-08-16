geral = []
continuar = ' '

while True:
    total_gols_ind = 0
    dados = {}
    dados['Nome'] = input('Nome do jogador: ')
    dados['Jogos'] = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    gols_indiv = []
    for c in range(0,dados['Jogos']):
        gols_indiv.append(int(input(f'Quantos gols na partida {c+1}? ')))
    dados['Gols'] = gols_indiv
    for c in range(0,len(gols_indiv)):
        total_gols_ind += gols_indiv[c]
    dados['Total'] = total_gols_ind
    geral.append(dados.copy())

    while continuar not in 'S' or continuar not in 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if continuar in 'S':
            break
        if continuar in 'N':
            break
    if continuar in 'N':
        break

print('-='*30)
print(f'{"cod":<4}{"nome":<15}{"gols":<20}total')
print('-'*50)
for c in range(0,len(geral)):
    print(f'{(c+1):>3} {geral[c]["Nome"]:<15}{str(geral[c]["Gols"]):<20}{geral[c]["Total"]}')
print('-'*50)

escolha = int()
while escolha != 999:
    escolha = int(input('Mostar dados de qual jogador? (999 para parar) '))
    if (escolha - 1) < len(geral) and (escolha - 1) >= 0:
        print(f'-- LEVANTAMENTO DO JOGADOR {geral[escolha - 1]["Nome"]}:')
        for c, k in enumerate(geral[escolha - 1]["Gols"]):
            print(f'No jogo {c+1} fez {k} gol(s).')
        print('-'*50)

