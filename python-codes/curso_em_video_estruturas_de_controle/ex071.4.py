valor = int(input('informe o valor a ser sacada: '))
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f'{nota50} notas de 50\n{nota20} notas de 20\n{nota10} notas de 10\n{nota1} notas de 1')