import sys
x = int(sys.stdin.readline())
a = [sys.maxsize for i in range(5000001)]
a[1] = 0
a[2] = 1
a[3] = 3
a[4] = 2
for i in range(3, x):
    for j in range(1, i):
        if j ** 2 <= i:
            if i % j == 0:
                t = i // j
                a[i+j] = min(t + a[i], a[i+j])
                a[i+t] = min(j + a[i], a[i+t])
        else:
            break
print(2, a[2])
print(4, a[4])
print(5, a[5])
print(10, a[10])
print(15, a[15])
print(30, a[30])
print(60, a[60])
print(61, a[61])
print(122, a[122])
print(244, a[244])
print(305, a[305])
print(610, a[610])
print(671, a[671])
print(1342, a[1342])
print(a[x])

