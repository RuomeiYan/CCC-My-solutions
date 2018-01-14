# Dynamic programming
import sys


def coin(x, y):
    if map_[x][y] == ".":
        return 0
    else:
        return int(map_[x][y])

while True:
    m, n = map(int, sys.stdin.readline().split())
    if m == 0: break
    map_ = [list(input()) for t1 in range(m)]
    # If any area is surrounded by asterisks from up, down and left, it should be replaced by asterisks
    xp = [[[False, False, False] for x in range(n)] for y in range(m)] # Down, up, left
    for i in range(0, m):
        for j in range(0, n):
            if map_[i][j] == "*":
                xp[i][j] = [True, True, True]
                for i_ in range(0,i-1):
                    xp[i_][j][0] = True
                for i_ in range(i+1,m):
                    xp[i_][j][1] = True
                for j_ in range(j+1,n):
                    xp[i][j_][2] = True
    for i in range(0, m):
        for j in range(0, n):
            if not False in xp[i][j]:
                map_[i][j] = "*"
    # End
    dp = [[0 for x in range(n)] for y in range(m)]
    # Initializes the first column
    dp[m - 1][0] = coin(m - 1, 0)
    for i in range(m - 2, -1, -1):
        if map_[i][0] == "*":
            break
        else:
            dp[i][0] = dp[i+1][0] + coin(i, 0)

    for t in range(1, n):
        max_column = [0 for t2 in range(m)]
        for i in range(m):
            if map_[i][t-1] != "*" and map_[i][t] != "*":
                temp_column = [0 for b in range(m)]
                temp_column[i] = dp[i][t-1] + coin(i, t)
                for x in range(i-1, -1, -1):
                    if map_[x][t] != "*":
                        temp_column[x] = temp_column[x+1] + coin(x,t)
                    else:
                        break
                for x in range(i+1, m):
                    if map_[x][t] != "*":
                        temp_column[x] = temp_column[x-1] + coin(x,t)
                    else:
                        break
                for x in range(m):
                    max_column[x] = max(max_column[x], temp_column[x])
        for p in range(m):
            dp[p][t] = max_column[p]

    for i in range(m):
        print(dp[i])
    print(dp[m-1][n-1])
