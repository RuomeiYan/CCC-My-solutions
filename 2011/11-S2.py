import sys
n = int(sys.stdin.readline())
stu = []
count = 0
for _ in range(n):
    stu.append(sys.stdin.readline())
for i in range(n):
    cor = sys.stdin.readline()
    if stu[i] == cor:
        count += 1
print(count)
