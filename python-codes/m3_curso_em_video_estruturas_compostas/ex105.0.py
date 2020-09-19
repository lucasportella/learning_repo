def notas(* individuais, sit=0):
    '''
    --> Função para analisar notas e situações de vários alunos.
    :param individuais: uma ou mais notas dos alunos (aceita várias)
    :param sit:valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situaççao da turma.
    '''
    total = 0
    total_notas = 0
    maior = int()

    for c in individuais:
        if total == 0:
            menor = c
        total += 1
        total_notas += c
        if c > maior:
            maior = c
        if c < menor:
            menor = c

    media = total_notas/total
    if sit == True:
        if media < 5:
            sit = 'RUIM'
        elif 5 < media < 7:
            sit = 'REGUlAR'
        elif 7 < media < 9:
            sit = "BOM"
        elif media >= 9:
            sit = "ÓTIMO"
        dados_em_dicionário = {'total': total, 'maior': maior, 'menor': menor,'media': media, 'situação': sit}
    else:
        dados_em_dicionário = {'total': total, 'maior': maior, 'menor': menor}
    return dados_em_dicionário


resp = notas(10, 8, 9, 5.6, 3.2, 9.8, sit = True)
print(resp)
help(notas)