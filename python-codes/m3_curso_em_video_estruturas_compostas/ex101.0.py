def voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return print(f"Com {idade} anos: VOTO NEGADO")
    elif 16 <= idade < 18 or idade >= 70:
        return print(f"Com {idade} anos: VOTO OPCIONAL")
    elif idade >= 18 and idade < 70:
        return print(f"Com {idade} anos: VOTO OBRIGATÓRIO")


print('--'*10)
voto(int(input("Em que ano você nasceu? ")))

