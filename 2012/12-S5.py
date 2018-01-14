import sys
r, c = map(int, sys.stdin.readline().split())
graph = [[0 for x in range(c)] for y in range(r)]
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = -1

t = 1
for i in range(r):
    if graph[i][0] == -1:
        t = -1
    graph[i][0] = t


t = 1
for i in range(c):
    if graph[0][i] == -1:
        t = -1
    graph[0][i] = t

for i in range(1, r):
    for j in range(1, c):
        if graph[i-1][j] == -1 and graph[i][j-1] == -1:
            graph[i][j] = -1


for i in range(1, r):
    for j in range(1, c):
        if graph[i][j] != -1:
            if graph[i-1][j] == -1:
                graph[i][j] = graph[i][j-1]
            elif graph[i][j-1] == -1:
                graph[i][j] = graph[i-1][j]
            else:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]
if graph[-1][-1] == -1:
    print(0)
else:
    print(graph[-1][-1])
