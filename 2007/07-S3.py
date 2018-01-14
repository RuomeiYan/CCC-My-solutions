n = int(input())
friends = {}
circles = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    friends[a] = b
for i, j in friends.items():
    for k in range(len(circles)):
        if i in circles[k]:
            circles[k].append(j)
            break
        if j in circles[k]:
            circles[k].append(i)
            break
    else:
        circles.append([i,j])
x, y = map(int, input().split())
while x!= 0 and y != 0:
    count = -1
    for i in circles:
        if x in i and y in i:
            while True:
                if x == y:
                    break
                count += 1
                x = friends[x]
            print("Yes", count)
            break
    else:
        print("No")
    x, y = map(int, input().split())



