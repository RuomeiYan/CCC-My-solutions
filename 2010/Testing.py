# 20/50
import sys
n = int(sys.stdin.readline())
edges = {}
tedges = {}
connect = {}

for i in range(n):
    pen = list(map(int, sys.stdin.readline().split()))
    connect[i] = []
    for j in range(1, pen[0]):
        if (pen[j], pen[j+1]) in tedges:
            edges[(tedges[(pen[j], pen[j+1])][0], i)] = pen[j + pen[0]]
            edges[(i, tedges[(pen[j], pen[j+1])][0])] = pen[j + pen[0]]
            connect[i].append(tedges[(pen[j], pen[j+1])][0])
            connect[tedges[(pen[j], pen[j+1])][0]].append(i)
            tedges.pop((pen[j+1], pen[j]))
            tedges.pop((pen[j], pen[j+1]))
        else:
            tedges[(pen[j], pen[j+1])] = [i, pen[j + pen[0]]]
            tedges[(pen[j+1], pen[j])] = [i, pen[j + pen[0]]]
    if (pen[1], pen[pen[0]]) in tedges:
        edges[(tedges[(pen[1], pen[pen[0]])][0], i)] = pen[-1]
        edges[(i, tedges[(pen[1], pen[pen[0]])][0])] = pen[-1]
        connect[i].append(tedges[pen[1], pen[pen[0]]][0])
        connect[tedges[pen[1], pen[pen[0]]][0]].append(i)
        tedges.pop((pen[1], pen[pen[0]]))
        tedges.pop((pen[pen[0]], pen[1]))
    else:
        tedges[(pen[1], pen[pen[0]])] = [i, pen[-1]]
        tedges[(pen[pen[0]], pen[1])] = [i, pen[-1]]

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
min_val = sys.maxsize
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

t = []
min_edg = ()
min_val = sys.maxsize
for i, j in edges.items():
    if j < min_val:
        min_val = j
        min_edg = i
t.append(min_edg[0])
t.append(min_edg[1])
ans2 = min_val
min_val = sys.maxsize
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
    print(t)
print(edges)
print(ans, ans2)
print(min(ans, ans2))
