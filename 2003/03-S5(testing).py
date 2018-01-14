c, r, d = map(int, input().split())
roads = []
for i in range(r):
    x, y, z = map(int, input().split())
    roads.append([z, x, y])
roads.sort(reverse=True)
des = [1]
for i in range(d):
    des.append(int(input()))
des = set(des)
visited = [1]
while not des.issubset(visited):
    for i in range(len(roads)):
        if roads[i][1] in visited and roads[i][2] not in visited:
            maxw = roads[i][0]
            visited.append(roads[i][2])
            roads.remove(roads[i])
            break
        if roads[i][1] not in visited and roads[i][2] in visited:
            maxw = roads[i][0]
            visited.append(roads[i][1])
            roads.remove(roads[i])
            break
print(maxw)



