import copy
roads = []
road = input()
points = {"A": "", "B": ""}
points2 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
while road != "**":               # input data
    roads.append(road)
    if road[0] not in points.keys():
        points[road[0]] = ""
    if road[1] not in points.keys():
        points[road[1]] = ""
    points[road[1]] += road[0]
    points[road[0]] += road[1]
    road = input()


def connect(start,end,points):      # Return if two points are connected
    connecting = start
    if start == end:
        return True
    counter = 0
    while counter != len(connecting):
        for i in points[connecting[counter]]:
            if i not in connecting:
                connecting += i
        counter += 1
    if end in connecting:
        return True
    return False

counter = 0
if connect("A","B",points):     # Find out which road is
    for i in roads:
        t = copy.deepcopy(points)          # Remove the road from the dictionary
        t[i[0]] = t[i[0]].replace(i[1], "")
        t[i[1]] = t[i[1]].replace(i[0], "")
        if not connect("A","B",t):
            print(i)
            counter += 1
print("There are", counter, "disconnecting roads.")


