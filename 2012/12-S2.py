import sys
ar = list(sys.stdin.readline())
ar.pop()
ar.reverse()
roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
pre = 0
ans = 0
for i in range(0, len(ar), 2):
    t = roman[ar[i]]
    if t >= pre:
        ans += int(ar[i+1]) * t
    else:
        ans -= int(ar[i+1]) * t
    pre = t
print(ans)
