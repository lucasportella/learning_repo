mais18 = m = fmenos20 = 0
while True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        m += 1
    if idade < 20 and sexo == 'F':
        fmenos20 += 1
    continuar = ' '
    while continuar not in 'SSIMNNAONÃO':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar in 'NNÃONAO':
        break
print('='*6,'FIM DO PROGRAMA','='*6)
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Total de homens cadastrados: {m}')
print(f'Total de mulheres com menos de 20 anos: {fmenos20}')