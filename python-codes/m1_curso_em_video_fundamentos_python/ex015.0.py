dias=int(input('Quantos dias alugados? '))
km=float(input('Quantos Km rodados? '))
diascalculo=dias*60
kmcalculo=km*0.15
total=diascalculo+kmcalculo
print('O total a pagar é de R${:.2f}'.format(total))