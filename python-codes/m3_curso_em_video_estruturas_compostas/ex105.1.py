def notas(* n, sit=False):
    dicio = {}
    dicio['total'] = len(n)
    dicio['maior'] = max(n)
    dicio['menor'] = min(n)
    dicio['soma'] = sum(n)
    dicio['media'] = sum(n)/len(n)
    if sit:
        if dicio['media'] >= 7:
            dicio['situação'] = 'BOM'
        elif 5 <= dicio['media'] < 7:
            dicio['situação'] = 'REGULAR'
        elif dicio['media'] < 5:
            dicio['situação'] = 'RUIM'

    return dicio


resp = notas(5.5, 9.5, 4.5, 1.5, sit = True)
print(resp)
