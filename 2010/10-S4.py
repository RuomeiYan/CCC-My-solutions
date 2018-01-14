import sys
n = int(sys.stdin.readline())
edges = {}
tedges = {}
connect = {}


def fence(v1, v2, cost, q):
    global connect, edges, tedges
    if (v1, v2) in tedges:
        if (v1, v2) in edges.keys():
            if cost < edges[(v1, v2)]:
                edges[(q, tedges[(v1, v2)][0])] = cost
                edges[(tedges[(v1, v2)][0], q)] = cost
        else:
            edges[(tedges[(v1, v2)][0], q)] = cost
            edges[(q, tedges[(v1, v2)][0])] = cost
            connect[q].append(tedges[(v1, v2)][0])
            connect[tedges[(v1, v2)][0]].append(q)
        tedges.pop((v1, v2))
        tedges.pop((v2, v1))
    else:
        tedges[(v1, v2)] = [q, cost]
        tedges[(v2, v1)] = [q, cost]


for i in range(n):
    pen = list(map(int, sys.stdin.readline().split()))
    connect[i] = []
    for j in range(1, pen[0]):
        fence(pen[j], pen[j+1], pen[j + pen[0]], i)
    fence(pen[1], pen[pen[0]], pen[-1], i)

t = []
min_edg = ()
min_val = sys.maxsize
for i, j in edges.items():
    if j < min_val:
        min_val = j
        min_edg = i
t.append(min_edg[0])
t.append(min_edg[1])
ans = min_val
while True:
    min_val = sys.maxsize
    min_edg = -2
    for i in t:
        for j in connect[i]:
            if j not in t and edges[(i,j)] < min_val:
                min_edg = j
                min_val = edges[(i,j)]
    if min_edg == -2:
        break
    t.append(min_edg)
    ans += min_val

if len(t) != n:
    ans = sys.maxsize


connect[-1] = []
for i, j in tedges.items():
    if (-1, j[0]) in edges.keys():
        if j[1] < edges[-1, j[0]]:
            edges[(-1, j[0])] = j[1]
            edges[(j[0], -1)] = j[1]
    else:
        edges[(-1, j[0])] = j[1]
        edges[(j[0], -1)] = j[1]
        connect[-1].append(j[0])
        connect[j[0]].append(-1)

# print(edges)
# print(tedges)
# print(connect[-1])
t = [-1]
min_edg = ()
min_val = sys.maxsize
for i in connect[-1]:
    if edges[(-1, i)] < min_val:
        min_val = edges[(-1, i)]
        min_edg = i
t.append(min_edg)
ans2 = min_val
while True:
    min_val = sys.maxsize
    min_edg = -2
    for i in t:
        for j in connect[i]:
            if j not in t and edges[(i,j)] < min_val:
                min_edg = j
                min_val = edges[(i,j)]
    if min_edg == -2:
        break
    t.append(min_edg)
    ans2 += min_val
print(ans, ans2)
# print(len(t))
print(min(ans, ans2))





