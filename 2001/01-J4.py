import copy
start = int(input())
end = int(input())
t = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
c = [0, 0]
for i in range(10):
    a[i] = copy.deepcopy(t)


def move(d,n):
    global c,s,end
    if s == end:
        return 0
    elif d == "l":        #move to the left
        for i in range(n):
            if s == end:
                break
            c[1] -= 1
            s += 1
            a[c[0]][c[1]] = s
    elif d == "r":        #move to the right
        for i in range(n):
            if s == end:
                break
            c[1] += 1
            s += 1
            a[c[0]][c[1]] = s
    elif d == "u":          #move up
        for i in range(n):
            if s == end:
                break
            c[0] -= 1
            s += 1
            a[c[0]][c[1]] = s
    elif d == "d":           #move down
        for i in range(n):
            if s == end:
                break
            c[0] += 1
            s += 1
            a[c[0]][c[1]] = s

    return c

a [4][4] = start
c = [4, 4]
s = start
for i in range(1,11):         #Build the spiral of numbers
    if i % 2 == 1:
        move("d",i)
        move("r",i)
    if i % 2 == 0:
        move("u",i)
        move("l",i)
minx = 20
miny = 20
maxx = -1
maxy = -1
for i in range(10):                #Find where the spiral is in the 2-dimension array(list)
    for j in range(10):
        if a[i][j] > 0:
            if i <= minx:
                minx = i
            if i >= maxx:
                maxx = i
            if j <= miny:
                miny = j
            if j >= maxy:
                maxy = j
for i in range(minx, maxx+1):       #Output the spiral
    for j in range(miny, maxy+1):
        if a[i][j] == 0:
            print("   ", end="")
        else:
            print("%3s" % (a[i][j]), end="")
    print()