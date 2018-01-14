import copy
# Initialization
cells = []
visited = [[False for y in range(9)] for x in range(10)]


# Return the content in the given coordinate
def coordinate(coord):
    global cells
    return cells[ord(coord[0]) - ord("A")][int(coord[1]) - 1]
# Input data
for _ in range(10):
    cells.append(input().split())
    for j in range(9):
        if cells[-1][j].isdigit():
            cells[-1][j] = int(cells[-1][j])
        elif len(cells[-1][j]) > 1:
            cells[-1][j] = [0] + cells[-1][j].split("+")
# Main program
sign = True
previous = copy.deepcopy(cells)
while sign:
    sign = False
    for i in range(10):
        for j in range(9):
            if not visited[i][j]:
                sign = True
                coord = chr(ord("A") + i) + str(j+1)

                if type(cells[i][j]) is int:
                    for h in range(10):
                        for k in range(9):
                            if type(cells[h][k]) is list and coord in cells[h][k]:
                                cells[h][k][0] += cells[i][j]
                                cells[h][k].remove(coord)
                    visited[i][j] = True

                elif cells[i][j] == "*":
                    for h in range(10):
                        for k in range(9):
                            if type(cells[h][k]) is list and coord in cells[h][k]:
                                cells[h][k] = "*"
                    visited[i][j] = True

                elif type(cells[i][j]) is list:
                    if len(cells[i][j]) == 1:
                        cells[i][j] = cells[i][j][0]
                    elif coord in cells[i][j]:
                        cells[i][j] = "*"

    # If there's no change, turn all lists into "*"(undefined)
    if cells == previous:
        for i in range(10):
            for j in range(9):
                if type(cells[i][j]) is list:
                    cells[i][j] = "*"
        break
    previous = copy.deepcopy(cells)
# Output data
for i in range(10):
    for j in range(9):
        print(cells[i][j],end=" ")
    print()


