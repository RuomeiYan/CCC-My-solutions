# Without Binary
import copy
r = int(input())
l = int(input())
board = [list(map(int, input().split())) for _ in range(r)]


def button(row1, row2):
    temp = copy.deepcopy(row2)
    for i in range(l):
        if row1[i] == row2[i]:
            temp[i] = 0
        else:
            temp[i] = 1
    return temp

possible = []
previous = [board.pop(0)]
for i in range(len(board)):
    possible = [board[i]]
    for j in previous:
        k = button(j, board[i])
        if k not in possible:
            possible.append(k)
    previous = possible

print(len(possible))