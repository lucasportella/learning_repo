def factorial(number):
    decrease_number = number
    result = 1
    while decrease_number > 0:
        if decrease_number > 1:
            print(f'{decrease_number} x ', end='')
        else:
            print('1 = ', end='')
        result *= decrease_number
        decrease_number -= 1
    print(result)


factorial(int(input('Digit a number for factorization: ')))