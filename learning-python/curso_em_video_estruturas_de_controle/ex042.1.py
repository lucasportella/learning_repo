print('\033[31;42m-=\033[m' * 10)
print('Analisador de triângulos')
print('\033[31;42m-=\033[m' * 10)
seg1=float(input('Primeiro segmento:'))
seg2=float(input('Segundo segmento: '))
seg3=float(input('Terceiro segmento:'))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos podem formar um triângulo',end=' ')
    if seg1 != seg2 and seg1 != seg3 and seg2 != seg3: #ou seg1 != seg2 != seg3 != seg1
        print('escaleno.')
    elif seg1 == seg2 != seg3 or seg1 == seg3 != seg2 or seg2 == seg3 != seg1:
        print('isósceles.')
    elif seg1 == seg2 == seg3: # ou só else:
        print('equilátero.')
else:
    print('Os segmentos não podem formar um triângulo.')