# Recursion after optimized
import copy
m = int(input())
q = int(input())
a = []
d = {}
t = 0
ans = []
for i in range(q):
    a.append(input())
    d[a[-1]] = int(input())
    t += d[a[-1]]


# To find the shortest time needed
def time(z):
    y = 0
    for i in z:
        x = 0
        for j in i:
            x = max(x,d[j])
        y += x
    return y


def recursion(r, b):
    global t, ans
    if len(b) == 0:
        y = time(r)
        if y < t:
            t = y
            ans = r
        return 0

    rc = copy.deepcopy(r)
    ac = copy.deepcopy(b)
    rc.append([])
    o = 0
    for _ in range(m):
        if len(ac) == 0:
            break
        o = max(d[ac[0]], o)
        rc[-1].append(ac[0])
        ac.pop(0)
        if len(rc[-1]) < m and len(ac) != 0 and d[ac[0]] < o:
            continue
        recursion(rc, ac)


recursion([], a)
print("Total Time:", t)
for i in ans:
    for j in i:
        print(j,end=" ")
    print()
