friends = {1:[6], 2:[6], 3:[4,5,6,15], 4:[3,5,6], 5:[3,4,6], 6:[1,2,3,4,5,7], 7:[6,8], 8:[7,9],
           9:[8,10,12], 10:[9,11], 11:[10,12], 12:[9,11,13], 13:[12,14,15], 14:[13], 15:[3,13],
           16:[17,18], 17:[16,18], 18:[16,17]}


def brush(x):
    if x in done:
        return 0
    for i in friends[x]:
        separation[i] = min(separation[i], separation[x] + 1)


def degrees(x):
    brush(x)
    done.append(x)
    current = 0
    while current < 51:
        current += 1
        for i, j in separation.items():
            if j == current:
                brush(i)


command = input()
while command != "q":
    if command == "i":
        x = int(input())
        y = int(input())
        if x not in friends:
            friends[x] = []
        if y not in friends:
            friends[y] = []
        friends[x].append(y)
        friends[y].append(x)
    elif command == "d":
        x = int(input())
        y = int(input())
        friends[x].remove(y)
        friends[y].remove(x)
    elif command == "n":
        x = int(input())
        print(len(friends[x]))
    elif command == "f":
        x = int(input())
        f = [x] + friends[x]
        for i in friends[x]:
            for j in friends[i]:
                if j not in f:
                    f.append(j)
        print(len(f)-len(friends[x])-1)
    elif command == "s":
        x = int(input())
        y = int(input())
        if x not in friends or y not in friends:
            print("Not connected")
            command = input()
            continue
        separation = {}
        done = []
        for i in friends:
            separation[i] = 51
        separation[x] = 0
        degrees(x)
        if separation[y] == 51:
            print("Not connected")
        else:
            print(separation[y])
    command = input()
