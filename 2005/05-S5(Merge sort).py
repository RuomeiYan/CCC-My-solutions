# Merge sort
import sys


def merge_sort(a, x, z):
    global I
    if x < z:
        y = (x + z) // 2
        merge_sort(a, x, y)
        merge_sort(a, y + 1, z)
        I += merge(a, x, y, z)


def merge(a, x, y, z):
    newa = [0 for _ in range(z - x + 1)]
    xx = x
    yy = y + 1
    k = 0
    total = 0
    while xx <= y and yy <= z:
        if a[xx] <= a[yy]:
            newa[k] = a[xx]
            k += 1
            xx += 1
        else:
            newa[k] = a[yy]
            k += 1
            yy += 1
            total += y + 1 - xx
    while xx <= y:
        newa[k] = a[xx]
        k += 1
        xx += 1
    while yy <= z:
        newa[k] = a[yy]
        k += 1
        yy += 1
    for xx in range(x, z + 1):
        a[xx] = newa[xx - x]
    return total

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
I = 0
merge_sort(a, 0, n - 1)
print("%.2f" % ((I + n) / n))







