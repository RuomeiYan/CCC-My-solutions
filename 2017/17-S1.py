import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
sum_a = sum(a)
sum_b = sum(b)
if sum_a == sum_b:
    print(n)
else:
    for i in range(-1, -n-1, -1):
        sum_a -= a[i]
        sum_b -= b[i]
        if sum_a == sum_b:
            print(n+i)
            break

