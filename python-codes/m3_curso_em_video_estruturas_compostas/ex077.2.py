lista = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRÁTIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
vogais = ('A','E','I','O','U')
for l in lista:
    print(f'\nNa palavra {l.lower()} temos',end=' ')
    for letra in l:
        if letra in 'AEIOUÁÂÃÉÊÕ':
            print(letra.lower(),end=' ')