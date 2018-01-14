# input
c, r, d = map(int, input().split())
roads = [[]] + [[0 for i in range(r + 1)] for j in range(r)]
for _ in range(r):
    x, y, w = map(int, input().split())
    if w > roads[x][y]:
        roads[x][y] = w
        roads[y][x] = w
des = [1]
for i in range(d):
    des.append(int(input()))

# prim's MST algorithm
val = [0 for i in range(c + 1)] # how much weight could get to each city
visited = [False for i in range(c + 1)] # if the city has been visited
val[1] = 100000 # there could be infinite weight in city one
maxt = 1 # now we have only reached city one
while maxt != -1:
    k = maxt # where are we now
    visited[maxt] = True # add the current location to the visited list
    ma = 0
    maxt = -1
    for t in range(1,c+1): # consider all the city
        # if that city's maximum possible weight is less than the minimum value of current city and the bridge btw them,
        # then that city's maximum possible weight should be replaced.
        if val[t] < min(val[k], roads[k][t]):
            val[t] = min(val[k], roads[k][t])
        # find out the unvisited city with the largest weight, set it to be the next city
        if val[t] >= ma and not visited[t]:
            ma = val[t]
            maxt = t
minw = 100000
for i in des:
    minw = min(minw, val[i])
print(minw)

