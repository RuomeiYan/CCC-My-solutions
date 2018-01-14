import sys
j = int(sys.stdin.readline())
a = int(sys.stdin.readline())
jerseys = [0]
size = {'S': 1, 'M': 2, 'L': 3}
for i in range(j):
    jerseys.append(size[sys.stdin.readline().strip()])
athletes = [4 for _ in range(j+1)]
for i in range(a):
    s, n = sys.stdin.readline().split()
    n = int(n)
    athletes[n] = min(size[s], athletes[n])
count = 0
for i in range(1, j+1):
    if jerseys[i] >= athletes[i]:
        count += 1
print(count)
