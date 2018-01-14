from collections import defaultdict, deque
from sys import stdin
input = stdin.readline

g = defaultdict(set)

_, M = map(int, input().split())

for _ in range(M):
    a, b = map(int, input().split())
    g[a].add(b)

def is_taller(p, q):
    queue = deque()
    seen = set()
    queue.append(p)
    while queue:
        v = queue.popleft()
        if v == q:
            return True
        if v not in g or v in seen:
            continue
        seen.add(v)
        queue.extend(g[v])
    return False

p, q = map(int, input().split())

if is_taller(p, q):
    print('yes')
elif is_taller(q, p):
    print('no')
else:
    print('unknown')
