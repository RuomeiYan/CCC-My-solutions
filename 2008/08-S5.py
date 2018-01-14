import sys
a = [[[[False for x in range(33)] for y in range(33)] for z in range(34)] for w in range(33)]
b = [[[[False for x in range(33)] for y in range(33)] for z in range(34)] for w in range(33)]


for w in range(30):
    for x in range(30):
        for y in range(30):
            for z in range(30):
                if b[w][x][y][z] is False and a[w][x][y][z] is False:
                    a[w + 2][x + 1][y][z + 2] = True
                    a[w + 1][x + 1][y + 1][z + 1] = True
                    a[w][x][y + 2][z + 1] = True
                    a[w][x + 3][y][z] = True
                    a[w + 1][x][y][z + 1] = True
                    b[w][x][y][z] = True

n = int(sys.stdin.readline())
for _ in range(n):
    A, B, C, D = map(int, sys.stdin.readline().split())
    if a[A][B][C][D]:
        print("Patrick")
    else:
        print("Roland")
