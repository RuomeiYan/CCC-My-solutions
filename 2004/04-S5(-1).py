# Dynamic programming
import sys
while True:
    # Input data
    m, n = map(int, sys.stdin.readline().split())
    if m == 0:
        break
    map0 = [list(input()) for t1 in range(m)]
    map_ = [[-1 for t2 in range(n)] for t3 in range(m)]
    for i in range(m):
        for j in range(n):
            if map0[i][j] == ".":
                map_[i][j] = 0
            elif map0[i][j] == "*":
                map_[i][j] = -1
            else:
                map_[i][j] = int(map0[i][j])

    dp = [[-1 for x in range(n)] for y in range(m)]
    # Initializes the first column
    dp[m - 1][0] = map_[m - 1][0]
    for i in range(m - 2, -1, -1):
        if map_[i][0] >= 0:
            dp[i][0] = dp[i+1][0] + map_[i][0]
        else:
            break

    # For each colume, try every gird in it
    for t in range(1, n):
        max_column = [-1 for t4 in range(m)]
        for i in range(m):
            # If it is reachable, try to move up and down
            if dp[i][t-1] >= 0 and map_[i][t] >= 0:
                temp_column = [-1 for b in range(m)]
                temp_column[i] = dp[i][t-1] + map_[i][t]
                for x in range(i-1, -1, -1):
                    if map_[x][t] >= 0:
                        temp_column[x] = temp_column[x+1] + map_[x][t]
                    else:
                        break
                for x in range(i+1, m):
                    if map_[x][t] >= 0:
                        temp_column[x] = temp_column[x-1] + map_[x][t]
                    else:
                        break
                for x in range(m):
                    max_column[x] = max(max_column[x], temp_column[x])
        for p in range(m):
            dp[p][t] = max_column[p]
    # Output result
    print(dp[m-1][n-1])

