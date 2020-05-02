sum = 0
num = 0
for c in range(1,501,2):
    if c % 3 == 0:
        sum += c
        num += 1
print(sum)
print(num)