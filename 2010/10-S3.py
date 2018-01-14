import math
L = 1000000
h = int(input())
houses = [int(input()) for _ in range(h)]
houses.sort()
k = int(input())
distances = [L - houses[-1] + houses[0]]
for i in range(1, h):
    distances.append(houses[i] - houses[i - 1])
while len(distances) > k + 1:
    adjacent = []
    for i in range(len(distances) - 1):
        adjacent.append(distances[i] + distances[i + 1])
    adjacent.append(distances[0] + distances[-1])
    t = adjacent.index(min(adjacent))
    if t == len(distances):
        distances[0] += distances.pop(-1)
    else:
        distances[t] += distances.pop(t + 1)
if k > h:
    print(0)
else:
    print(math.ceil(min(distances) / 2))