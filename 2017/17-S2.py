import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
if n % 2 == 0:
    low = a[:n//2]
    high = a[n//2:]
    high.reverse()
    ans = []
    for i in range(n//2):
        ans.append(low.pop())
        ans.append(high.pop())
    for i in ans:
        print(i,end=" ")
    print()
else:
    low = a[:n//2+1]
    high = a[n//2+1:]
    high.reverse()
    ans = []
    for i in range(n//2):
        ans.append(low.pop())
        ans.append(high.pop())
    ans.append(low[0])
    for i in ans:
        print(i,end=" ")
    print()
