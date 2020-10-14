def leiaInt(texto):
    while True:
        try:
           inteiro = int(input(texto))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            break
        except:
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        else:
            return inteiro

def leiaFloat(texto):
    while True:
        try:
            real = float(input(texto))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            continue
        except:
            print('ERRO: por favor, digite um número real válido.')
            continue
        else:
            return real
        

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
