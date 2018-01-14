# Largest Common Prefix
def lcs(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return i
    return min(len(a), len(b))

n = int(input())
for _ in range(n):
    st = input()
    t = []
    for i in range(len(st)):
        t.append(st[i:])
    t.sort()
    ans = len(t[0]) + 1
    for i in range(1,len(t)):
        ans += len(t[i]) - lcs(t[i], t[i-1])
    print(ans)
