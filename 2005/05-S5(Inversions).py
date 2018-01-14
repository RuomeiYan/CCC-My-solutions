# counting inversions
import sys
n = int(sys.stdin.readline())
iv = 0
scores = [int(sys.stdin.readline()) for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if scores[i] > scores[j]:
            iv += 1
print("%.2f" % ((iv + n) / n))
