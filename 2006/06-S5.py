# Copied from http://mmhs.ca/ccc/2006/CCC2006s5OriginofLifeV2.txt
import sys


def to_int():  # Change life2 into an integer
    out = 0
    power = 1
    for it in range(1, m + 1):
        for jt in range(1, n + 1):
            out += life2[it][jt] * power
            power *= 2
    return out


def to_array(x):  # Change an integer into life1 array
    global life1, m, n
    for it in range(1, m + 1):
        for jt in range(1, n + 1):
            life1[it][jt] = x % 2
            x //= 2


def next_gen(x):
    to_array(x)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            sum = life1[i-1][j-1] + life1[i-1][j] + life1[i-1][j+1] + life1[i][j-1] + \
                life1[i][j+1] + life1[i+1][j-1] + life1[i+1][j] + life1[i+1][j+1]
            if life1[i][j] == 1:
                if sum < a or sum > b:
                    life2[i][j] = 0
                else:
                    life2[i][j] = 1
            else:
                if sum > c:
                    life2[i][j] = 1
                else:
                    life2[i][j] = 0
    return to_int()


def get_edens():
    is_eden = [True for _ in range(size)]
    for it in range(size):
        is_eden[next_gen(it)] = False
    for it in range(size):
        if is_eden[it]:
            eden.append(it)


def count_from_eden(start):
    found = False
    for count in range(1, 51):
        if found:
            break
        for i in range(len(eden)):
            if eden[i] == start:
                found = True
                t = count - 1
                break
            else:
                eden[i] = next_gen(eden[i])
    if found:
        return t
    else:
        return -1

m, n, a, b, c = map(int, sys.stdin.readline().split())
life1 = [[0 for t1 in range(n + 2)] for t3 in range(m + 2)]
life2 = [[0 for t2 in range(n + 2)] for t4 in range(m + 2)]
size = pow(2, m * n)
for i in range(1, m + 1):
    s = sys.stdin.readline()
    for j in range(1, n + 1):
        if s[j - 1] == "*":
            life2[i][j] = 1
original = to_int()
eden = []
get_edens()
print(count_from_eden(original))




