expressao = input('Digite a expressão: ').strip()
quant_parenteses_abrir = expressao.count('(')
quant_parenteses_fechar = expressao.count(')')
parenteses_para_fechar = 0
distancia_entre_parenteses = 0
diferenca = 0
erros = []

if quant_parenteses_abrir == quant_parenteses_fechar:
    caracter_anterior = ''
    for caracter in expressao:
        if caracter == ')' and parenteses_para_fechar == 0:
            validade = False
            erros.append('Você fechou parenteses antes de abrir')
            break
        if caracter == '(':
            parenteses_para_fechar += 1
            distancia_entre_parenteses += 1
            continue
        if caracter != ')':
            distancia_entre_parenteses += 1
            caracter_anterior = caracter
            continue
