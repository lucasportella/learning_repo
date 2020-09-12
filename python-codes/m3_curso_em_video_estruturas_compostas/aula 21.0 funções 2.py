def factorial(number):
    print(f'{number} x {number - 1} x',end=' ')
    c = number - 1
    result = number * (number - 1)
    while c > 1:
        c -= 1
        print(f'{c}',end=' ')
        if c > 1:
            print('x',end=' ')
        result = result * c
    print(f'= {result}')


factorial(int(input('Digit a number for factorization: ')))