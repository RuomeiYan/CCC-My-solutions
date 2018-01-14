import sys

for _ in range(int(sys.stdin.readline())):
    n, b, w = map(int, sys.stdin.readline().split())
    pins = []
    for i in range(n):
        pins.append(int(sys.stdin.readline()))
    for i in range(n):
        for j in range(i + 1, min(i + w, n)):
            pins[i] += pins[j]

    dp = [[pins[0]]]
    for i in range(1, n):
        if pins[i] > dp[0][i-1]:
            dp[0].append(pins[i])
        else:
            dp[0].append(dp[0][i-1])

    for i in range(1, b):
        dp.append([])
        for j in range(w):
            dp[i].append(dp[i-1][j])
        for j in range(w, n):
            dp[i].append(max(dp[i][j-1], pins[j] + dp[i-1][j-w]))

    print(dp[b-1][n-1])
