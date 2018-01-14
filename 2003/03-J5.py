# input data
f = int(input())
r = int(input())
c = int(input())
m = []
room = []


# Determine the area of one room(count), turn that room into all "I"s
def label(tr, tc):
    global count
    if tr < 0 or tr >= r or tc < 0 or tc >= c or m[tr][tc] == "I":
        return 0
    m[tr][tc] = "I"
    count += 1
    for i in range(tr-1,tr+2):
        for j in range(tc-1,tc+2):
            if not (tr == i and tc == j):
                if 0 <= i < r and 0 <= j < c:
                    label(i,j)

# input the map
for i in range(r):
    m.append(list(input()))

# Determines the area of all the rooms,
# and put areas into a list "room"
for i in range(r):
    for j in range(c):
        if m[i][j] == ".":
            count = 0
            label(i,j)
            room.append(count)
room.sort(reverse=True)

# Calculates how many rooms could have flooring installed
count = 0
for i in room:
    if i <= f:
        f -= i
        count += 1
    else:
        break
# Output data
if count == 1:
    print("%d room, %d square metre(s) left over" % (count,f))
else:
    print("%d rooms, %d square metre(s) left over" % (count,f))

