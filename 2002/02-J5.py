rows = int(input())
columns = int(input())
backyard = []
moves = []
location = []
for i in range(rows):          # input data
    backyard.append("")
    backyard[i] = list(input())
m = int(input())
for i in range(m):
    moves.append(input())


def path(move, r, c, d):           # To check one point is possible to be the initial position
    global backyard, rows, columns, location       # Returns a boolean value and the final position
    if not ((0 <= r < rows) and (0 <= c < columns)) or backyard[r][c] == "X":
        return False
    if len(move) == 0:
        location = [r, c]
        return True
    if move[0] == "F":
        if d == 1: return path(move[1:],r-1,c,d)
        if d == 2: return path(move[1:],r,c+1,d)
        if d == 3: return path(move[1:],r+1,c,d)
        if d == 4: return path(move[1:],r,c-1,d)
    elif move[0] == "L":
        if d == 1: d = 4
        else: d -= 1
        return path(move[1:],r,c,d)
    else:
        if d == 4: d = 1
        else: d += 1
        return path(move[1:],r,c,d)


def directions(moves,i,j,d):       # Try one direction
    if path(moves,i,j,d):
        backyard[location[0]][location[1]] = "*"

for i in range(rows):             # Check every grid in the backyard
    for j in range(columns):
        if backyard[i][j] != "X":
            directions(moves,i,j,1)
            directions(moves,i,j,2)
            directions(moves,i,j,3)
            directions(moves,i,j,4)


for i in range(rows):          # Output the answer
    for j in range(columns):
        print(backyard[i][j],end="")
    print()


