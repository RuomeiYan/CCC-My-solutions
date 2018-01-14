# Copied from mmhs.ca/ccc/index.htm
import sys
import itertools
import copy
n = int(sys.stdin.readline())
p = [[0,0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
p_indices = [i for i in range(n+1)]


distances = []
for i in itertools.combinations(p_indices, 2):
    distances.append([(p[i[0]][0]-p[i[1]][0])**2 + (p[i[0]][1]-p[i[1]][1])**2, i[0], i[1]])
distances.sort()

best = [0 for i in range(n+1)]
pre = 0
for i in distances:
    if pre != i[0]:
        pbest = copy.deepcopy(best)
    if i[1] == 0:
        best[0] = max(best[0], pbest[i[2]] + 1)
    else:
        best[i[1]] = max(best[i[1]], pbest[i[2]] + 1)
        best[i[2]] = max(best[i[2]], pbest[i[1]] + 1)
    pre = i[0]
print(best[0])
