nome=str(input('Olá, me diga seu nome: ')).strip()
if nome == 'Lucas':
    print('Bonito nome.')
elif nome == 'João' or nome == 'Maria' or nome == 'José':
    print('Nome popular no Brasil.')
elif nome in 'Ana Claudia Cláudia Jordete Marcia Márcia Jaqueline':
    print('belo nome feminino')
else:
    print('Nome normal.')
print('Tenha um bom dia.')