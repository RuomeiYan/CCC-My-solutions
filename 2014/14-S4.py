# Copied from mmhs.ca/ccc/index.htm
import sys
n = int(sys.stdin.readline())
l = int(sys.stdin.readline())
glasses = []
xs = set()
ys = set()
for i in range(n):
    glasses.append(list(map(int, sys.stdin.readline().split())))
    xs.add(glasses[-1][0])
    xs.add(glasses[-1][2])
    ys.add(glasses[-1][1])
    ys.add(glasses[-1][3])
xs = sorted(list(xs))
ys = sorted(list(ys))
dict_xs = {xs[i]: i for i in range(len(xs))}
dict_ys = {ys[i]: i for i in range(len(ys))}
g = [[0 for y in range(len(ys))] for x in range(len(xs))]
for i in glasses:
    for j in range(dict_xs[i[0]], dict_xs[i[2]]):
        g[j][dict_ys[i[1]]] += i[4]
        g[j][dict_ys[i[3]]] -= i[4]

count = 0
for i in range(len(xs)):
    if g[i][0] >= l:
        count += (ys[1] - ys[0]) * (xs[1] - xs[0])
    for j in range(1, len(ys)):
        g[i][j] += g[i][j-1]
        if g[i][j] >= l:
            count += (ys[j+1] - ys[j]) * (xs[i+1] - xs[i])
print(count)


