import sys
lights = [[0, 0]]
for i in range(int(sys.stdin.readline())):
    t = int(sys.stdin.readline())
    if t:
        if lights[-1][1] == 0:
            lights[-1][0] = i
            lights[-1][1] = i
        lights[-1][1] += 1
    else:
        if lights[-1][1] != 0:
            lights.append([0, 0])
# For test case 4 and 9:
if lights[-1][1] == 0:
    lights.pop()

n = len(lights)
dp = [0 for _ in range(n)]
dp[0] = 4 - lights[0][1] + lights[0][0]
dp[1] = min(4 - lights[1][1] + lights[1][0] + dp[0], lights[1][0] - lights[0][1])
for i in range(2, n):
    dp[i] = min(4 - lights[i][1] + lights[i][0] + dp[i-1], lights[i][0] - lights[i-1][1] + dp[i-2])
print(dp[-1])


