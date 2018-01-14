board = [None]
moves = []
# Initializes the board
for i in range(1,9):
    board.append([None])
    for j in range(1,9):
        board[i].append(".")

data = input().split()

# Create board a,b or c
if data[0] == "a":
    board[4][4] = "w"
    board[5][4] = "b"
    board[4][5] = "b"
    board[5][5] = "w"
elif data[0] == "b":
    for i in range(1,9):
        board[i][i] = "b"
        board[9-i][i] = "w"
else:
    for i in range(1,9):
        board[i][3] = "b"
        board[i][4] = "b"
        board[i][5] = "w"
        board[i][6] = "w"

# Creates the "moves" list
for i in range(2,len(data)-1,2):
    moves.append((int(data[i]),int(data[i+1])))


# To determine if a coordinate is valid
def valid(x,y):
    if 1 <= x <= 8 and 1 <= y <= 8:
        return True
    return False


def move(color, r, c):
    board[r][c] = color
    if color == "w":
        opp = "b"
    else:
        opp = "w"
    # Check horizontally
    # To the right
    for i in range(c+1,9):
        if board[r][i] == opp:
            continue
        elif board[r][i] == color:
            for j in range(c+1,i):
                board[r][j] = color
            break
        else:
            break
    # To the left
    for i in range(c-1,0,-1):
        if board[r][i] == opp:
            continue
        elif board[r][i] == color:
            for j in range(i+1,c):
                board[r][j] = color
            break
        else:
            break

    # Check vertically
    # Down
    for i in range(r+1,9):
        if board[i][c] == opp:
            continue
        elif board[i][c] == color:
            for j in range(r+1,i):
                board[j][c] = color
            break
        else:
            break
    # Up
    for i in range(r-1,0,-1):
        if board[i][c] == opp:
            continue
        elif board[i][c] == color:
            for j in range(i+1,r):
                board[j][c] = color
            break
        else:
            break

    # Check diagonally
    # Downright
    for i in range(1,8):
        if valid(r+i,c+i):
            if board[r+i][c+i] == opp:
                continue
            elif board[r+i][c+i] == color:
                for j in range(1,i):
                    board[r+j][c+j] = color
                break
            else:
                break
        else:
            break
    # Downleft
    for i in range(1,8):
        if valid(r+i,c-i):
            if board[r+i][c-i] == opp:
                continue
            elif board[r+i][c-i] == color:
                for j in range(1,i):
                    board[r+j][c-j] = color
                break
            else:
                break
        else:
            break
    # Upleft
    for i in range(1,8):
        if valid(r-i,c-i):
            if board[r-i][c-i] == opp:
                continue
            elif board[r-i][c-i] == color:
                for j in range(1,i):
                    board[r-j][c-j] = color
                break
            else:
                break
        else:
            break
    # Upright
    for i in range(1,8):
        if valid(r-i,c+i):
            if board[r-i][c+i] == opp:
                continue
            elif board[r-i][c+i] == color:
                for j in range(1,i):
                    board[r-j][c+j] = color
                break
            else:
                break
        else:
            break
color = "b"
for i in moves:
    move(color,i[0],i[1])
    if color == "b":
        color = "w"
    else:
        color = "b"
        
# Count
black = 0
white = 0
for i in range(1,9):
    for j in range(1,9):
        if board[i][j] == "b":
            black += 1
        elif board[i][j] == "w":
            white += 1
print(black,end=" ")
print(white)


