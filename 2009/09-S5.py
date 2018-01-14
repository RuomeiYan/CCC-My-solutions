import sys
Y = int(sys.stdin.readline())
X = int(sys.stdin.readline())
K = int(sys.stdin.readline())
grids = [[0 for yt in range(Y + 1)] for xt in range(X + 1)]
for _ in range(K):
    x, y, r, b = map(int, sys.stdin.readline().split())
    for i in range(max(1, x-r), min(X, x+r)+1):
        for j in range(max(1, y-r), min(Y, y+r)+1):
            if (i-x) ** 2 + (j-y) ** 2 <= r ** 2:
                grids[i][j] += b
max_num = 0
max_b = 0
for i in range(1, X+1):
    for j in range(1, Y+1):
        if grids[i][j] > max_b:
            max_b = grids[i][j]
            max_num = 0
        if grids[i][j] == max_b:
            max_num += 1
print(max_b)
print(max_num)
