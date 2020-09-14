from datetime import date

def voto(ano_nascimento):
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return print(f"Com {idade} anos: VOTO NEGADO")
    elif idade >= 16 and idade < 18:
        return print(f"Com {idade} anos: VOTO OPCIONAL")
    elif idade >= 18 and idade < 70:
        return print(f"Com {idade} anos: VOTO OBRIGATÓRIO")
    elif idade >= 70:
        return print(f"Com {idade} anos: VOTO OPCIONAL")


print('--'*10)
voto(int(input("Em que ano você nasceu? ")))

