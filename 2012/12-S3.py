import sys
n = int(sys.stdin.readline())
readings = {}
for i in range(n):
    t = int(sys.stdin.readline())
    if t in readings:
        readings[t] += 1
    else:
        readings[t] = 1
data = []
for i, j in readings.items():
    data.append((i, j))
data.sort(key= lambda x:x[1], reverse=True)
fre = data[0][1]
first = []
sec = []
for i, j in enumerate(data):
    if j[1] == fre:
        first.append(j[0])
    else:
        if len(first) > 1:
            break
        for t in range(i, len(data)):
            if data[t][1] == j[1]:
                sec.append(data[t][0])
            else:
                break
        break

if len(first) > 1:
    print(max(first) - min(first))
else:
    for k in range(len(sec)):
        sec[k] = abs(sec[k] - first[0])
    print(max(sec))
