# Official solution...Case #4 is off by 0.13

import math
n = int(input())
chips = []
for i in range(n):
    x, y = map(int, input().split())
    chips.append([x,y])


def diameter(x, y):
    maximum = 0
    for i in range(n):
        maximum = max((chips[i][0]-x) ** 2 + (chips[i][1]-y) ** 2, maximum)
    return 2 * math.sqrt(maximum)

delta = 2000
x = 0
y = 0
while delta > 10**(-6):
    if diameter(x+delta, y) < diameter(x, y):
        x += delta
    if diameter(x-delta, y) < diameter(x, y):
        x -= delta
    if diameter(x, y+delta) < diameter(x, y):
        y += delta
    if diameter(x, y-delta) < diameter(x, y):
        y -= delta
    delta *= .9
print(x,y)
print("%.2f" % round(diameter(x,y), 2))