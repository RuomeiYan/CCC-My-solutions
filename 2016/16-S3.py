import sys


def check():
    for i in pho:
        if not visited[i]:
            return False
    return True

n, p = map(int, sys.stdin.readline())
pho = [int(sys.stdin.readline()) for _ in range(p)]
g = [False * n] * n
for i in range(n):
    x, y = map(int, sys.stdin.readline())
    g[x][y] = True
    g[y][x] = True
visited = [False * n]
q = [pho.pop()]
while q:
    t = q.pop()
    for i in range(n):
        if g[t][i]:


