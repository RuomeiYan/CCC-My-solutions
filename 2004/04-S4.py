import sys


def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2) ** (1/2)


def move(forward, turn):
    global drt, min_dist
    for i in range(forward):
        loc[drt[0][1]] += 1 * drt[0][0]
        min_dist = min(min_dist, distance(loc, end))
    if turn == "L":
        drt[0], drt[1] = drt[1], drt[0]
        drt[1][0] *= -1
    elif turn == "R":
        drt[0], drt[1] = drt[1], drt[0]
        drt[0][0] *= -1
    elif turn == "U":
        drt[0], drt[2] = drt[2], drt[0]
        drt[2][0] *= -1
    elif turn == "D":
        drt[0], drt[2] = drt[2], drt[0]
        drt[0][0] *= -1
    elif turn == "E":
        return True
    return False

loc = list(map(int, sys.stdin.readline().split()))
end = tuple(map(int, sys.stdin.readline().split()))
min_dist = distance(loc, end)
drt = [[1, 0], [1, 1], [1, 2]]  # Forward, left, top
while True:
    forw, direction = sys.stdin.readline().split()
    forw = int(forw)
    if move(forw, direction):
        break
print(round(min_dist, 2))