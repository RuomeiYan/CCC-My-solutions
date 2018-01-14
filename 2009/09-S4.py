import sys
n = int(sys.stdin.readline())
roads = {}
connect = {}
for _ in range(int(sys.stdin.readline())):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    if (a, b) in roads.keys():
        roads[(a, b)] = min(c, roads[(a, b)])
        roads[(b, a)] = min(c, roads[(b, a)])
    else:
        roads[(a, b)] = c
        roads[(b, a)] = c
        connect[a] = [b]
        connect[b] = [a]
        connect[a].append(b)
        connect[b].append(a)
price = [0 for i in range(n)]
for _ in range(int(sys.stdin.readline())):
    z , p = map(int, sys.stdin.readline().split())
    price[z - 1] = p
d = int(sys.stdin.readline()) - 1

cost = [0 for i in range(n)]
visited = [False for i in range(n)]
visited[d] = True
