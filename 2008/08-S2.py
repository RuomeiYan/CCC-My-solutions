import math
while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    for i in range(1, n):
        count += math.floor(math.sqrt(n**2 - i**2))
    count *= 4
    count += 4 * n + 1
    print(count)