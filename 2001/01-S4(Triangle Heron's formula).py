# I really don't know how to solve this problem.
# The following code is copied from Milliken Mills High School CCC website
# http://mmhs.ca/ccc/index.htm

import math
n = int(input())
chips = []
for i in range(n):
    x, y = map(int, input().split())
    chips.append([x,y])


def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)

ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a = distance(chips[i][0], chips[i][1], chips[j][0], chips[j][1])
            b = distance(chips[i][0], chips[i][1], chips[k][0], chips[k][1])
            c = distance(chips[j][0], chips[j][1], chips[k][0], chips[k][1])
            s = (a + b + c) / 2
            if s == 0 or a**2 + b**2 - c**2 < 0 or b**2 + c**2 - a**2 < 0 or c**2 + a**2 - b**2 < 0:
                d = max(a,b,c)
            else:
                d = 2*a*b*c/(4*math.sqrt(s*(s-a)*(s-b)*(s-c)))
            if d > ans:
                ans = d
print("%.2f" % round(ans, 2))