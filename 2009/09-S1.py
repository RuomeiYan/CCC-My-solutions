import math
a = int(input())
b = int(input())
count = 0


def is_int(x):
    if abs(x - round(x)) < 0.00001:
        return True
    return False

for i in range(math.floor(a ** (1/3)),math.ceil((b+1) ** (1/3))):
    if is_int(math.sqrt(i ** 3)) and a <= i ** 3 <= b:
        count += 1

print(count)