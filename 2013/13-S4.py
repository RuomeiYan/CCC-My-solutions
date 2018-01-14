import sys
import copy


def compare(p, q):
    front = copy.deepcopy(hei[p])
    v = [False for i in range(n+1)]
    while front:
        if q in front:
            return True
        t = []
        for i in front:
            v[i] = True
            for j in hei[i]:
                if not v[j]:
                    t.append(j)
        front = copy.deepcopy(t)
    else:
        return False

n, m = map(int, sys.stdin.readline().split())
if m == 0:
    p, q = map(int, sys.stdin.readline().split())
    print("unknown")
else:
    hei = [[] for i in range(n+1)]
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        hei[x].append(y)
    p, q = map(int, sys.stdin.readline().split())
    if compare(p, q):
        print('yes')
    elif compare(q, p):
        print('no')
    else:
        print('unknown')
