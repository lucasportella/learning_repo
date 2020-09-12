def factorial(number=1):
    result = 1
    for c in range(number,0,-1):
        result *= c
    return result

while True:
    print(factorial(int(input('Digit a number for factorization: '))))
    continuar =(str(input('Continue? Type only yes or no: '))).strip().lower()
    if continuar in "no":
        break