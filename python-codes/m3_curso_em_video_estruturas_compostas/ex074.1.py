from random import sample
a = tuple(sample(range(0,10), 5))
print(f'Valores: {a}')
print(f'Maior valor é {max(a)} e o menor valor é {min(a)}.')