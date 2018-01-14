import sys
# input
c, r, d = map(int, sys.stdin.readline().split())
roads = {}
for _ in range(r):
    x, y, w = map(int, sys.stdin.readline().split())
    if x > y:
        x, y = y, x
    if (x, y) in roads.keys():
        roads[(x, y)] = max(roads[(x,y)], w)
    else:
        roads[(x, y)] = w
des = [1]
for i in range(r + 1, r + d + 1):
    des.append(int(sys.stdin.readline()))
