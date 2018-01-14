import sys
Y = int(sys.stdin.readline())
X = int(sys.stdin.readline())
K = int(sys.stdin.readline())
grids = [[0 for yt in range(Y + 1)] for xt in range(X + 1)]
for _ in range(K):
    x, y, r, b = map(int, sys.stdin.readline().split())
    for i in range(max(1, x-r), min(X, x+r)+1):
        for j in range(max(1, y-r), y+1):
            if (i-x) ** 2 + (j-y) ** 2 <= r ** 2:
                grids[i][j] += b
                break
        if (i-x) ** 2 + (Y-y) ** 2 <= r ** 2:
            continue
        for j in range(min(Y-1, y+r), y-1, -1):
            if (i-x) ** 2 + (j-y) ** 2 <= r ** 2:
                grids[i][j+1] -= b
                break
# print(grids)
max_num = 0
max_b = 0
for i in range(1, X+1):
    for j in range(2, Y+1):
        grids[i][j] += grids[i][j-1]
# print(grids)
for i in range(1, X+1):
    for j in range(1, Y+1):
        if grids[i][j] > max_b:
            max_b = grids[i][j]
            max_num = 0
        if grids[i][j] == max_b:
            max_num += 1
print(max_b)
print(max_num)
