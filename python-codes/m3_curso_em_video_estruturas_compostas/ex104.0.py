def leiaInt(texto):
    numero = ''
    while numero is not int:
        numero = (input(texto))
        if numero.isnumeric():
            numero = int(numero)
            return numero
        if numero is not int:
            print("ERRO! Digite um número inteiro válido.")
        

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
