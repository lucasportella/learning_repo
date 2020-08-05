lista = []
dicio = {}
dicio["Nome"] = ""
dicio["Sexo"] = ""
dicio["Idade"] = ""
soma_idade = int()
continuar = ' '
mulheres_cadastradas = []
contador_acima_media = 0
#loop raíz:
while True:
    #adição de dados(nome,sexo(esse com verificação de erro), idade):
    dicio["Nome"] = (input('Nome: '))
    while True:
        dicio["Sexo"] = str(input('Sexo: [M/F] ')).upper().strip()
        if dicio["Sexo"] == 'M':
            break
        elif dicio["Sexo"] == 'F':
            mulheres_cadastradas.append(dicio["Nome"][:])
            break
        elif dicio["Sexo"] not in 'M' or 'F':
            print('Erro! Por favor, digite apenas M ou F')
    dicio["Idade"] = int(input('Idade: '))
    soma_idade += dicio["Idade"]
    lista.append(dicio.copy())

   #continuar:
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

#análise dos dados:
print('-='*30)
print(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma_idade/(len(lista))
print(f'B) A média de idade é de {media} anos.')
if len(mulheres_cadastradas) >0:
    print(f'C) As mulheres cadastradas foram ',end='')
else:
    print(f'C) Nenhuma mulher foi cadastrada.',end='')
for c in mulheres_cadastradas:
    print(f'{c} ',end='')
for c in lista:
    if c["Idade"] > media:
        contador_acima_media += 1
if contador_acima_media > 0:
    print(f'\nD) Lista das pessoas que estão acima da média:')
for c in lista:
    if c["Idade"] > media:
        print(f'   nome = {c["Nome"]}; sexo = {c["Sexo"]}; idade = {c["Idade"]}')
if contador_acima_media > 0:
    print('<< ENCERRADO >>')
else:
    print('\n<< ENCERRADO >>')

