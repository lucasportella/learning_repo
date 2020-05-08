print('\033[31;42m-=\033[m' * 10)
print('Analisador de triângulos')
print('\033[31;42m-=\033[m' * 10)
seg1=float(input('Primeiro segmento:'))
seg2=float(input('Segundo segmento: '))
seg3=float(input('Terceiro segmento:'))
if seg1 == seg2 == seg3: #em outras linguagens tem q fazer assim: seg1 == seg2 and seg2 == seg3
                         #seg1 != seg2 != seg3 --> não pode, pois existe a possibilidade de
                         #seg1 == seg3 ex: seg1 == 1 seg2 == 2 seg3 == 1
    print('Os segmentos podem formar um triângulo equilátero')
elif seg2 == seg3 or seg1 == seg2 or seg1 ==seg3:
    print('Os segmentos podem formar um triângulo isósceles.')
elif seg1 < seg2+seg3 and seg2 < seg1+seg3 and seg3 < seg1+seg2:
    print('Os segmentos podem formar um triângulo escaleno.')
elif seg1 >= (seg2+seg3) or seg2 >= (seg1+seg3) or seg3 >= (seg1+seg2):
#else:
    print('Os segmentos NÃO podem formar um triângulo.')
