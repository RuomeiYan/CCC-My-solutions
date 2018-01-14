def motel(c):
    global count
    if motels[c] == 7000:
        count += 1
        return 0
    for i in range(c+1, len(motels)):
        if motels[c]+b >= motels[i] >= motels[c]+a:
            motel(i)
        elif motels[i] >= motels[c]+b:
            return 0
        else:
            continue

count = 0
a = int(input())
b = int(input())
n = int(input())
motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
for i in range(n):
    motels.append(int(input()))
motels.sort()
motel(0)
print(count)