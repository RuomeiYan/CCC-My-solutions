a = []
for i in range(3):
    a.append(int(input()))
a.remove(max(a))
a.remove(min(a))
print(a[0])
