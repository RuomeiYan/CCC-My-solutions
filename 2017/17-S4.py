import sys
n, m, d = map(int, sys.stdin.readline().split())
tup = [[-1 for i in range(n+1)] for _ in range(n+1)]
active = []
min_c = sys.maxsize
for t1 in range(m):
    x, y, c = map(int, sys.stdin.readline().split())
    if t1 < n-1:
        if x < y:
            active.append((x, y))
        else:
            active.append((y, x))
    tup[x][y] = c
    tup[y][x] = c
    if c < min_c:
        min_c = c
        q = [x, y]


connected = [False] * (n+1)
connected[q[0]] = True
connected[q[1]] = True
if q[0] < q[1]:
    tubes = [(q[0], q[1])]
else:
    tubes = [(q[1], q[0])]
while len(q) < n:
    p = 0
    t = 0
    min_c = sys.maxsize
    for i in q:
        for j in range(1, n + 1):
            if not connected[j] and -1 < tup[i][j] < min_c:
                min_c = tup[i][j]
                t = j
                p = i
    q.append(t)
    connected[t] = True
    if p < t:
        tubes.append((p, t))
    else:
        tubes.append((t, p))


count = 0
for i in range(n-1):
    if tubes[i] in active:
        count += 1
print(n-1-count)

