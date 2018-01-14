a = int(input())
b = int(input())
c = int(input())
t = int(input())
ways = []
for i in range(0,t//a+1):
    for j in range(0, t//b+1):
        for k in range(0, t//c+1):
            if (i*a+j*b+k*c)<=t:
                ways.append([i,j,k])
ways.remove([0,0,0])
for i in ways:
    print(i[0],"Brown Trout,",i[1],"Northern Pike,",i[2],"Yellow Pickerel")
print("Number of ways to catch fish:",len(ways))