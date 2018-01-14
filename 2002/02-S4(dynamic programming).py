m=int(input())
q=int(input())
names=[]
times=[]
for _ in range(q):
    names.append(input())
    times.append(int(input()))
# find best time
best=[10**9 for _ in range(q+1)]
best[0]=0
groups=[[] for _ in range(q+1)]
for i in range(1,q+1):
    crosstime=0
    for j in range(1,min(i,m)+1):
        crosstime=max(crosstime,times[i-j])
        if best[i]>best[i-j]+crosstime:
            best[i]=best[i-j]+crosstime
            groups[i]=groups[i-j]+[i]
# print stuff
print("Total Time:",best[q])
# print names
i=0
for j in groups[-1]:
    print(" ".join(names[i:j]))
    i=j
