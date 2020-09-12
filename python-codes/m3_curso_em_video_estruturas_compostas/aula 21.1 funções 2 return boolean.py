def even_verifier(number):
    if number % 2 == 0:
        return True
    else:
        return False


num = int(input("Type a number: "))
if even_verifier(num):
    print("It's even!")
else:
    print("It's odd!")
