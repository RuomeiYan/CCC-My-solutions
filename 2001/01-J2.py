x = int(input())
m = int(input())
n = 0
for i in range(1,m):
    if (x*i) % m == 1:
        n = i
        break
if n == 0:
    print("No such integer exists.")
else:
    print(n)