num1=float(input('Primeiro número: '))
num2=float(input('Segundo número: '))
if num1 > num2:
    print('\033[4;31;42mO primeiro valor é maior.\033[m')
elif num2 > num1:
    print('\033[1;33;45mO segundo valor é maior.\033[m')
else:
    print('Os valores são iguais.')
