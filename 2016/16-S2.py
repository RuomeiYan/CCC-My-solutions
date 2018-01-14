import sys
choice = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort(reverse=True)
b.sort(reverse=True)
if choice == 1:
    ans = 0
    for i in range(n):
        ans += max(a[i], b[i])
    print(ans)

else:
    i = 0
    j = 0
    ans = 0
    for _ in range(n):
        if a[i] > b[j]:
            ans += a[i]
            i += 1
        else:
            ans += b[j]
            j += 1
    print(ans)


