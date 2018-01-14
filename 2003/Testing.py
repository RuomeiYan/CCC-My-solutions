import sys
# input
c, r, d = map(int, sys.stdin.readline().split())
roads = {}
for _ in range(r):
    x, y, w = map(int, sys.stdin.readline().split())
    if x > y:
        x, y = y, x
    if (x, y) in roads.keys():
        roads[(x, y)] = max(roads[(x,y)], w)
    else:
        roads[(x, y)] = w
des = [1]
for i in range(r + 1, r + d + 1):
    des.append(int(sys.stdin.readline()))

# prim's MST algorithm
val = [0 for i in range(c + 1)]  # how much weight could get to each city
val[1] = 100000  # there could be infinite weight in city one
maxt = 1  # Start at the first city
cities = {1}  # Set
for i in range(2, c + 1):
    cities.add(i)           # Set with all cities in it
visited = {1}
while maxt != -1:
    k = maxt # where are we now
    ma = 0
    maxt = -1
    visited.add(k)
    for t in cities - visited: # consider all the city
        # if that city's maximum possible weight is less than the minimum value of current city and the bridge btw them,
        # then that city's maximum possible weight should be replaced.
        if k > t:
            tem = (t, k)
        else:
            tem = (k, t)
        if tem in roads.keys():
            tt = min(val[k], roads[tem])
            val[t] = max(tt, val[t])

        # find out the unvisited city with the largest weight, set it to be the next city
        if val[t] >= ma:
            ma = val[t]
            maxt = t

minw = 100000
for i in des:
    minw = min(minw, val[i])
print(minw)


