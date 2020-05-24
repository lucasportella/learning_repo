p1=(float(input('Digite o preço do produto R$')))
#p2=p1-(p1*0.05)
p2=p1-(p1*5/100)
print('Esse produto com 5% de desconto fica com o',end=
' preço de R${:.2f}'.format(p2))