from datetime import date

def voto(ano_nascimento):
    ano_nascimento = date.today().year - ano_nascimento
    if ano_nascimento < 16:
        return "NÃO VOTA"
    elif ano_nascimento >= 16 and ano_nascimento < 18:
        return "VOTO OPCIONAL"
    elif ano_nascimento >= 18 and ano_nascimento < 70:
        return "VOTO OBRIGATÓRIO"
    elif ano_nascimento >= 70:
        return "VOTO OPCIONAL"


print('--'*10)
nasc = int(input("Em que ano você nasceu? "))
idade = date.today().year - nasc
print(f"Com {idade} anos: {voto(nasc)}")
