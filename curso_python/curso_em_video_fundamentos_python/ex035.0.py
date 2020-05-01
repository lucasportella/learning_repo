print('\033[7;34;42m-=\033[m'*20)
print('Analisador de Triângulos')
print('\033[7;32;47m-=\033[m'*20)
seg1=float(input('Primeiro segmento: '))
seg2=float(input('Segundo segmento: '))
seg3=float(input('Terceiro segmento: '))
if  seg1 < (seg2 + seg3) and seg2 < (seg1 +seg3) and seg3 < (seg2 + seg1):
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')