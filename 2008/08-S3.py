# BFS
n = int(input())


def move(x, y):
    if map_[x][y] == "*":
        labels[x][y] = -1
        return 0
    t1 = labels[x-1][y]
    t2 = labels[x+1][y]
    t3 = labels[x][y-1]
    t4 = labels[x][y+1]
    if map_[x][y] == "+":
        labels[x-1][y] = min(labels[x-1][y], labels[x][y] + 1)
        labels[x+1][y] = min(labels[x+1][y], labels[x][y] + 1)
        labels[x][y-1] = min(labels[x][y-1], labels[x][y] + 1)
        labels[x][y+1] = min(labels[x][y+1], labels[x][y] + 1)
    elif map_[x][y] == "|":
        labels[x-1][y] = min(labels[x-1][y], labels[x][y] + 1)
        labels[x+1][y] = min(labels[x+1][y], labels[x][y] + 1)
    elif map_[x][y] == "-":
        labels[x][y-1] = min(labels[x][y-1], labels[x][y] + 1)
        labels[x][y+1] = min(labels[x][y+1], labels[x][y] + 1)
    if labels[x-1][y] != t1:
        will_visit.append([x-1, y])
    if labels[x+1][y] != t2:
        will_visit.append([x+1, y])
    if labels[x][y-1] != t3:
        will_visit.append([x, y-1])
    if labels[x][y+1] != t4:
        will_visit.append([x, y+1])

for _ in range(n):
    r = int(input())
    c = int(input())

    map_ = [["*" for k in range(c+2)]]
    for i1 in range(r):
        map_.append(["*"]+list(input())+["*"])
    map_.append(["*" for t in range(c+2)])

    labels = [[10**10 for x1 in range(c+2)] for y1 in range(r+2)]
    labels[1][1] = 1

    will_visit = [[1,1]]
    while len(will_visit) > 0:
        move(will_visit[0][0], will_visit[0][1])
        will_visit.pop(0)

    if labels[r][c] == 10**10:
        print(-1)
    else:
        print(labels[r][c])


