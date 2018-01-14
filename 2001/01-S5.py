m = int(input())
n = int(input())
a = []
b = []
ans = []
for i in range(n):
    a.append(input())
for _ in range(n):
    b.append(input())


def recursion(x, ac, bc, r):
    global ans
    if x == 0:
        if ac == bc:
            ans = r
        return 0

    x -= 1
    for i in range(n):
        recursion(x, ac+a[i], bc+b[i], r+[i])


for i in range(1, m):
    recursion(i, "", "", [])
    if ans:
        break

if ans:
    print(len(ans))
    for i in ans:
        print(i+1)
else:
    print("No solution.")


