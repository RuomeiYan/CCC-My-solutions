# 3:0 1:1
import sys
import copy
my = int(sys.stdin.readline())
n = int(sys.stdin.readline())
teams = [0 for i in range(5)]
com = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
for _ in range(n):
    a, b, sa, sb = map(int, sys.stdin.readline().split())
    if a < b:
        com.remove((a, b))
    else:
        com.remove((b, a))
    if sa == sb:
        teams[a] += 1
        teams[b] += 1
    elif sa > sb:
        teams[a] += 3
    else:
        teams[b] += 3

pos = [teams]
for i in com:
    t = []
    for j in pos:
        q = copy.deepcopy(j)
        q[i[0]] += 3
        t.append(q)
        q = copy.deepcopy(j)
        q[i[1]] += 3
        t.append(q)
        q = copy.deepcopy(j)
        q[i[0]] += 1
        q[i[1]] += 1
        t.append(q)
    pos = copy.deepcopy(t)

count = 0
for i in pos:
    if i[my] == max(i) and i.count(i[my]) == 1:
        count += 1
print(count)
