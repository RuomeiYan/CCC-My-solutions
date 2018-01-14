w = int(input())
h = int(input())
p = float(input())
q = float(input())
done = {0: [p], 1: [q], 2: [], 3: []}
count = 1
k = q/(w-p)
cs = 1
while True:
    print(cs,q," * ",count, k)
    if cs % 2 == 1:
        wt, ht = h, w
    else:
        wt, ht = w, h
    cs = (cs+1) % 4
    t = (ht-q)/k
    if t > wt or t < 0:
        cs = (cs+1) % 4
        t = ht - wt * k - q
    print(cs, t, " & ", count)
    if (cs % 2 == 0 and 5 <= t <= w - 5) or (cs % 2 == 1 and 5 <= t <= h-5):
        count += 1
        q = t
        k = 1/k
    else:
        break

    if q in done[cs]:
        count = 0
        break
    else:
        done[cs].append(t)

print(count)


# y = kx + b
# (y - q) = k (x - w)
# y = h or x = 0
#    (h - q)/ k + w = x  when the next location is on the adjacent side
#    the value we want is w-x

