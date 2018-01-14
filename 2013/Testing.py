import sys
import math
x = int(sys.stdin.readline())
a = [-1 for i in range(5000001)]
a[1] = 0
a[2] = 1
a[3] = 3
a[4] = 2


def optimize(x):
    if a[x] > -1:
        return a[x]
    min_point = sys.maxsize
    for q in range(x//2, x):
        i = x - q
        if q % i == 0:
            min_point = min(optimize(q) + q // i, min_point)
    a[x] = min_point
    return min_point

print(optimize(x))
