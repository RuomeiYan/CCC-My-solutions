import copy
l, w, x = map(int, input().split())
l1 = [(0,0,1,0), (1,0,1,1), (1,1,2,1), (2,1,2,0), (2,0,3,0)]


# Build the fractals
def fractals(l, d, w):
    r = copy.deepcopy(l)
    for i in l:
        r.append((w-i[1], w-i[0], w-i[3], w-i[2]))
        r.append((i[0]+w, i[1]+w, i[2]+w, i[3]+w))
        r.append((2*w+i[1], w-i[0], 2*w+i[3], w-i[2]))
        r.append((i[0]+2*w, i[1], i[2]+2*w, i[3]))
    return r


# Output data
def output(map, x, c):
    x *= 3**l / w
    r = []
    for i in map:
        if i[0] == x and i[2] == x:
            if i[3] > i[1]:
                for j in range(i[1]*c,i[3]*c+1):
                    r.append(j+1)
            else:
                for j in range(i[3]*c,i[1]*c+1):
                    r.append(j+1)
        elif i[0] <= x <= i[2] or i[2] <= x <= i[0]:
            r.append(i[1]*c+1)
    for i in sorted(list(set(r))):
        print(int(i), end=" ")

if l == 0:
    print(1)
elif l == 1:
    output(l1,x,int(w/3))
elif l == 2:
    l2 = fractals(l1,1,3)
    output(l2,x,int(w/9))
elif l == 3:
    l2 = fractals(l1,1,3)
    l3 = fractals(l2,1,9)
    output(l3,x,int(w/27))
elif l == 4:
    l2 = fractals(l1,1,3)
    l3 = fractals(l2,1,9)
    l4 = fractals(l3,1,27)
    output(l4,x,int(w/81))

