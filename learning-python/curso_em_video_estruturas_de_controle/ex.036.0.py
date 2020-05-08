print('\033[4;33;45mPrograma de financiamento\033[m')
casa=float(input('Qual o valor da casa? '))
salário=float(input('Qual o seu salário? '))
tempo=int(input('Quantos anos para pagar? '))
tempo_meses=int(tempo * 12)
salário_usável=salário * 0.30
prestação = casa/tempo_meses
cálculo=salário_usável * tempo_meses
if cálculo >= casa:
    print('Empréstimo aprovado e o valor da prestação será {:.2f}'.format((prestação)))
elif cálculo < casa:
    print('Empréstimo negado.')