import sys
import itertools
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = set(a)
if len(a) == 2:
    print(1, 1)
elif len(b) == len(a):
    sums = []
    for i in itertools.combinations(a, 2):
        sums.append(sum(i))
    sums.sort()
    t = 0
    l = len(sums)
    count = 0
    max_l = 0
    for i in range(sums[0], sums[-1]+1):
        q = 0
        for j in range(t, l):
            if sums[j] == i:
                q += 1
            else:
                t = j
                break
        if q == 1:
            continue
        else:
            if q > max_l:
                max_l = q
                count = 1
            elif q == max_l:
                count += 1
    if max_l > 1:
        print(max_l, count)
    else:
        print(1, n * (n-1) // 2)
else:
    sums = []
    for i in itertools.combinations(b, 2):
        sums.append(sum(i))
    d = []
    for i in b:
        t = a.count(i)
        if t > 1:
            d.append((i, t))
            for _ in range(t//2):
                sums.append(i*2)
        for i in itertools.combinations(d, 2):
            for _ in range(min(i[0][1], i[1][1])-1):
                sums.append(i[0][0]+i[0][1])
    sums.sort()
    t = 0
    l = len(sums)
    count = 0
    max_l = 0
    for i in range(sums[0], sums[-1]+1):
        q = 0
        for j in range(t, l):
            if sums[j] == i:
                q += 1
            else:
                t = j
                break
        if q == 1:
            continue
        else:
            if q > max_l:
                max_l = q
                count = 1
            elif q == max_l:
                count += 1
    if max_l > 1:
        print(max_l, count)
    else:
        print(1, n * (n-1) // 2)