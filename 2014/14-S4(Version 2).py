import sys
n = int(sys.stdin.readline())
t = int(sys.stdin.readline())

#-1000000000 is small enough to be at index 0 after sorting
line = [[0]]
#-1000000000 is just a place holder
segy = [-1000000000]

for i in range(n):
    x1,y1,x2,y2,val=map(int,sys.stdin.readline().split())
    line.append([x1,y1,y2,val])        #Incoming side
    line.append([x2,y1,y2,-val])       #Outgoing side
    segy.append(y1)
    segy.append(y2)

line.sort()

#Remove duplicates and sort
segy = list(set(segy))
segy.sort()

#Coordinate Compression with a hash table
findy = {}
for i in range(1, len(segy)):
    findy[segy[i]] = i

yaxis=[0 for i in range(len(segy) + 1)]

ans=0

#Sweep Line loop
for i in range(1, len(line)):
    for j in range(1, len(segy)):
        if yaxis[j] >= t:
            ans += (segy[j + 1] - segy[j]) * (line[i][0] - line[i - 1][0])
    for j in range(findy[line[i][1]], findy[line[i][2]]):
        yaxis[j] += line[i][3]

print(ans)
