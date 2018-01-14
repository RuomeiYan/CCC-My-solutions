import sys
n = int(sys.stdin.readline())
roads = {}
while True:
    x, y = map(int, sys.stdin.readline().split())
    if x == 0:
        break
    if (x-1) in roads.keys():
        roads[x-1].append(y-1)
    else:
        roads[x-1] = [y-1]

paths = [0 for i in range(n)]
paths[0] = 1
for t in range(n - 1):
    if t in roads.keys():
        for j in roads[t]:
            paths[j] += paths[t]

print(paths[n-1])


