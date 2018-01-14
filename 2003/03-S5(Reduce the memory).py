import time
# input
c, r, d = map(int, input().split())
roads = {}
for _ in range(r):
    x, y, w = map(int, input().split())
    if x > y:
        x, y = y, x
    if (x, y) in roads.keys():
        roads[(x, y)] = max(roads[(x,y)], w)
    else:
        roads[(x, y)] = w
des = [1]
for i in range(d):
    des.append(int(input()))

# prim's MST algorithm
val = [0 for i in range(c + 1)] # how much weight could get to each city
val[1] = 100000 # there could be infinite weight in city one
maxt = 1 # now we have only reached city one
cities = {1}
for i in range(2,c+1):
    cities.add(i)
visited = {1}
while maxt != -1:
    if time.clock() > 1:
        break
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
        if tem in roads.keys() and val[t] < min(val[k], roads[tem]):
            val[t] = min(val[k], roads[tem])
        # find out the unvisited city with the largest weight, set it to be the next city
        if val[t] >= ma:
            ma = val[t]
            maxt = t

minw = 100000
for i in des:
    minw = min(minw, val[i])
print(minw)


