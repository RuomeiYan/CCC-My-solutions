n = int(input())
computers = []
for _ in range(n):
    computers.append(input().split())
    computers[-1][1] = int(computers[-1][1]) * 2 + int(computers[-1][2]) * 3 + int(computers[-1][3])
if n == 1:
    print(computers[0][0])
elif n != 0:
    maximum = max(computers, key=lambda x: x[1])[1]
    first = []
    for x in range(n):
        if computers[x][1] == maximum:
            first.append(computers[x][0])
            computers[x][1] = 0

    if len(first) == 1:
        second = []
        maximum = max(computers,key=lambda x: x[1])[1]
        for x in computers:
            if x[1] == maximum:
                second.append(x[0])
        second.sort()
        print(first[0])
        print(second[0])
    else:
        first.sort()
        print(first[0])
        print(first[1])