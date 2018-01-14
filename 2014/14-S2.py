import sys
from collections import defaultdict
n = int(sys.stdin.readline())
a1 = sys.stdin.readline().split()
a2 = sys.stdin.readline().split()
d = defaultdict(list)
for i in range(n):
    d[a1[i]].append(a2[i])
for i, k in d.items():
    if len(k) != 1 or k[0] == i or i != d[k[0]][0]:
        print('bad')
        break
else:
    print('good')
