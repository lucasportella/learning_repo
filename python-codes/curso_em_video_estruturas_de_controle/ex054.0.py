from datetime import date
ano = date.today().year
maior = 0
menor = 0
anoc = 1
for c in range(1,8,1):
    anonasc= int(input('Ano de nascimento da {}ª pessoa: '.format(anoc)))
    anoc += 1
    if anonasc < ano:
        if (ano - anonasc) >= 18:
            maior += 1
        elif (ano - anonasc) < 18:
            menor += 1
    if anonasc > ano:
        print('Erro. O ano de nascimento não pode ser maior que o ano atual.')
print('Pessoas que já atinjiram a maioridade: {} \nPessoas que não atingiram a maioridade ainda: {}'.format(maior,menor))


