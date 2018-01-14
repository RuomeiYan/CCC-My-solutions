import sys


def count_depth(pre):
    global ans
    ans += 20
    nxt = []
    for j in pre:
        for i in orders[j]:
            if i in orders.keys():
                nxt.append(i)
    if len(nxt) > 0:
        count_depth(nxt)

n = int(sys.stdin.readline())
for _ in range(n):
    k = int(sys.stdin.readline())
    points = []
    orders = {}
    for t in range(k):
        points.append(sys.stdin.readline().strip())
    points = [points[-1]] + points
    while True:
        for i in range(len(points) - 2):
            if points[i] == points[i + 2]:
                if points[i] in orders.keys():
                    orders[points[i]].append(points[i + 1])
                else:
                    orders[points[i]] = [points[i+1]]
                points.pop(i)
                points.pop(i)
                break
        else:
            break
    ans = 0
    start = [points[0]]
    count_depth(start)
    print(k * 10 - ans)

