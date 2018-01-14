from math import ceil, floor

a = int(input())
b = int(input())

print(1 if a == b else floor(pow(b, 1/6)) - ceil(pow(a, 1/6)) + 1)
