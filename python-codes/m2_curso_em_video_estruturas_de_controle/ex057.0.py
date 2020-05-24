sexo = str(input('Diga seu sexo [M/F]: ')).strip().lower()
while sexo not in 'm,f,masculino,feminino':
    print('Erro. Digite apenas M ou F para o sexo')
    sexo = str(input('Diga seu sexo [M/F]: ')).strip()
if sexo in 'm,masculino':
    print('Sexo masculino registrado com sucesso.')
elif sexo in 'f,feminino':
    print('Sexo feminino registrado com sucesso')