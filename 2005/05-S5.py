# Binary + Insertion 40/100
import sys
n = int(sys.stdin.readline())
s = 0


def insert_(c, x, y):
    global s
    # insert one element in an given interval
    for i in range(x, y + 1):
        if scores[i] <= c:
            scores.insert(i, c)
            s += i
            return 0
    else:
        if y == len(scores) - 1:
            scores.append(c)
            s += len(scores) - 1
        else:
            scores.insert(y + 1, c)
            s += y + 1


def binary(low, high, c):
    # Find the closet interval! [low, high]
    if high - low <= 5:
        insert_(c, low, high)
        return 0
    mid = (high + low) // 2
    if scores[mid] < c:
        binary(low, mid - 1, c)
    elif scores[mid] > c:
        binary(mid + 1, high, c)
    else:
        insert_(c, low, high)
        return 0

if n == 1:
    print(1)
else:
    scores = [int(sys.stdin.readline())]
    for i in range(0, n - 1):
        # High == coordinate of the last char
        binary(0, i, int(sys.stdin.readline()))
    print("%.2f" % (s / n + 1))