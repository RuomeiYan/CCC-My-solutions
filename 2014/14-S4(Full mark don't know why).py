# Copied from mmhs.ca/ccc/index.htm
import sys
rects = []
xs = []
ys = []

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())

for i in range(n):
	rect = list(map(int,sys.stdin.readline().split()))
	xs.append(rect[0])
	ys.append(rect[1])
	xs.append(rect[2])
	ys.append(rect[3])
	rects.append(rect)

itox = sorted(list(set(xs)))
itoy = sorted(list(set(ys)))

xtoi = {itox[i]:i for i in range(len(itox))}
ytoi = {itoy[i]:i for i in range(len(itoy))}

da = [[0]*len(itox) for i in range(len(itoy))]

for i in range(n):
	for j in range(ytoi[rects[i][1]],ytoi[rects[i][3]]):
		da[j][xtoi[rects[i][0]]] += rects[i][4]
		da[j][xtoi[rects[i][2]]] -= rects[i][4]

ans = 0
for i in range(len(itoy)-1):
	for j in range(len(itox)-1):
		da[i][j+1] = da[i][j] + da[i][j+1]
		if da[i][j] >= t:
			ans += (itoy[i+1] - itoy[i]) * (itox[j+1] - itox[j])

print(ans)
