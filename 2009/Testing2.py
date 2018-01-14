import sys
n = int(sys.stdin.readline())
roads = [[-1 for x in range(n + 1)] for y in range(n + 1)]
con = {}
for _ in range(int(sys.stdin.readline())):
    a, b, c = map(int, sys.stdin.readline().split())
    if a > b:
        a, b = b, a
    if roads[a][b] == -1:
        roads[a][b] = c
        if a in con:
            con[a].append(b)
        else:
            con[a] = [b]
        if b in con:
            con[b].append(a)
        else:
            con[b] = [a]
    else:
        roads[a][b] = min(c, roads[a][b])
price = [-1 for i in range(n + 1)]
for _ in range(int(sys.stdin.readline())):
    z , p = map(int, sys.stdin.readline().split())
    price[z] = p
d = int(sys.stdin.readline())

cost = [sys.maxsize for i in range(n + 1)]
visited = [False for i in range(n + 1)]
cur = d
cost[d] = 0
while True:
    visited[cur] = True
    min_cost = sys.maxsize
    nex = -1
    for i in con[cur]:
        if i < cur:
            ti, tcur = cur, i
        else:
            ti, tcur = i, cur
        if roads[tcur][ti] > -1 and visited[i] is False:
            cost[i] = min(roads[tcur][ti] + cost[cur], cost[i])
            if cost[i] < min_cost:
                min_cost = cost[i]
                nex = i
    if nex == -1:
        break
    cur = nex


min_cost = sys.maxsize
for i in range(n + 1):
    if price[i] > -1:
        price[i] += cost[i]
        if price[i] < min_cost:
            min_cost = price[i]
print(min_cost)
