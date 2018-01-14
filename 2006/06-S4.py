import sys


def identity():
    standard = [t for t in range(1, n + 1)]
    for i in range(1, n + 1):
        if group[i][1:] == standard:
            return i
    return False


def inverse(id):
    for i in range(1, n + 1):
        if id not in group[i]:
            return False
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            if group[i][j] == id:
                break
        else:
            return False
    return True


def associativity():
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            for k in range(j, n + 1):
                if group[group[i][j]][k] != group[i][group[j][k]] or \
                   group[group[j][k]][i] != group[j][group[k][i]] or \
                   group[group[k][i]][j] != group[k][group[i][j]]:
                    return False
    return True

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    group = [[-1]]
    for _ in range(n):
        group.append([-1] + list(map(int, sys.stdin.readline().split())))
    id = identity()
    if id is False:
        print("no")
        continue
    if inverse(id) is False:
        print("no")
        continue
    if associativity() is False:
        print("no")
        continue
    print("yes")

