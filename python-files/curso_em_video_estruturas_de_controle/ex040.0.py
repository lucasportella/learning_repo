nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))
media=float((nota1+nota2)/2)
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1,nota2,media))
if media >= 7.0:
    print('Você passou!')
#elif media < 7.0 and media >= 5.0:
elif 7 > media >= 5:
    print('Voce está em recuperação.')
elif media < 5.0:
    print('Você está reprovado.')
