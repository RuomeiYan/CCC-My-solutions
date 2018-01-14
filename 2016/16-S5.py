import sys
import copy
n, t = map(int, sys.stdin.readline().split())
a = list(sys.stdin.readline().strip())
for i in range(n):
    a[i] = int(a[i])


def change(t):
    global c
    if c[t]:
        c[t] = 0
    else:
        c[t] = 1

for _ in range(t):
    c = [0 for j in range(n)]
    if a[0]:
        change(1)
        change(-1)
    if a[-1]:
        change(-2)
        change(0)
    for i in range(1, n-1):
        if a[i]:
            change(i-1)
            change(i+1)
    a = copy.deepcopy(c)

for i in range(n):
    print(c[i],end='')
print()
