# Copied from mmhs.ca/ccc/index.htm
import sys
a = int(sys.stdin.readline())
p = int(sys.stdin.readline())
airports = [0 for i in range(a+1)]
count = 0
for _ in range(p):
    t = int(sys.stdin.readline())
    # print(t, airports)
    while t > 0 and airports[t] > 0:
        q = airports[t]
        airports[t] += 1
        t -= q
    if t <= 0:
        break
    else:
        airports[t] = 1
        count += 1
print(count)
