def factorial(number=1):
    result = 1
    for c in range(number,0,-1):
        result *= c
    return result


print(factorial(int(input('Digit a number for factorization: '))))
