x1, y1, x2, y2 = map(int, input().split())
n = int(input())
buildings = []
for _ in range(n):
    buildings.append(list())
    temp = list(map(int, input().split()))
    for i in range(temp[0]):
        buildings[-1].append([temp[2 * i + 1], temp[2 * i + 2]])


def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 == x2:
        k2 = (y3 - y4) / (x3 - x4)
        b2 = y3 - k2 * x3
        return x1, k2 * x1 + b2
    if x3 == x4:
        k1 = (y1 - y2) / (x1 - x2)
        b1 = y1 - k1 * x1
        return x3, k1 * x3 + b1
    k1 = (y1 - y2) / (x1 - x2)
    b1 = y1 - k1 * x1
    k2 = (y3 - y4) / (x3 - x4)
    b2 = y3 - k2 * x3
    if k1 == k2:
        return False, False
    else:
        x = (b2 - b1) / (k1 - k2)
        y = k1 * x + b1
        return x, y


def online(x, y, x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    if x1 <= x <= x2 and y1 <= y <= y2:
        return True
    return False


count = 0
for i in buildings:
    corners = len(i)
    sign = False
    for j in range(corners):
        if j == corners - 1:
            nxt = i[0]
        else:
            nxt = i[j + 1]
        j = i[j]
        if j[0] == nxt[0] and x1 == x2:
            continue
        if j[1] == nxt[1] and y1 == y2:
            continue
        xt, yt = intersection(x1, y1, x2, y2, j[0], j[1], nxt[0], nxt[1])
        if xt and online(xt, yt, x1, y1, x2, y2) and online(xt, yt, j[0], j[1], nxt[0], nxt[1]):
            sign = True
            break
    if sign:
        count += 1

print(count)

