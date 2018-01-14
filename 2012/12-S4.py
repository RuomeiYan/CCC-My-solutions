import sys
import copy
n = int(sys.stdin.readline())


def convert(b):
    t = 0
    for i, j in enumerate(b):
        for k in j:
            t += i * n ** (k - 1)
    return t


def convert_b(d):
    q = [[] for _ in range(n)]
    for i in range(1, n+ 1):
        t = d % n
        d //= n
        q[t].append(i)
    for i in range(n):
        q[i].sort(reverse=True)
    return q


def tr(c, x, y):
    global front, nxt
    c = convert_b(c)
    if len(c[x]) > 0 and (len(c[y]) == 0 or c[x][-1] < c[y][-1]):
        if c[x][-1] == n and y < x:
            return 0
        c[y].append(c[x].pop())
        t = convert(c)
        if not visit[t]:
            nxt.append(t)
            visit[t] = True


def move(b):
    tr(b, 0, 1)
    for i in range(1, n-1):
        tr(b, i, i-1)
        tr(b, i, i+1)
    tr(b, -1, -2)


while n > 0:
    visit = [False for i in range(n ** n)]
    a = list(map(int, sys.stdin.readline().split()))
    front = [convert([[a[i]] for i in range(n)])]
    visit[front[0]] = True
    re = convert([[i] for i in range(1, n+1)])
    if visit[re]:
        print(0)
        n = int(sys.stdin.readline())
        continue
    count = 0
    while True:
        nxt = []
        for i in front:
            move(i)
        front = copy.deepcopy(nxt)
        count += 1
        if re in front:
            print(count)
            break
        if not nxt:
            print("IMPOSSIBLE")
            break
    n = int(sys.stdin.readline())
