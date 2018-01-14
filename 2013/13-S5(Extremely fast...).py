import math
import sys
x = int(sys.stdin.readline())
ans = 0
while True:
    if x == 1:
        print(ans)
        break
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            ans += i - 1
            x -= x // i
            break
    else:
        x -= 1
        ans += x
