def even_verifier(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(even_verifier(int(input("Type a number to know if it's even or not: "))))