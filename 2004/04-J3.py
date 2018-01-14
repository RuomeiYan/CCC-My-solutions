n = int(input())
m = int(input())
a = []
b = []
for _ in range(n):
    a.append(input())
for _ in range(m):
    b.append(input())
for i in range(n):
    for j in range (m):
        print(a[i],"as",b[j])