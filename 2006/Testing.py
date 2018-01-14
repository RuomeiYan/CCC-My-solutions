def count_around(g,x,y):  # count how many dead and alive cells there are around the cell(x,y)
    dead = 0
    alive = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if not (x == i and y == j):
                if 0 <= i < m and 0 <= j < n:
                    if g[i][j] == ".":
                        dead += 1
                    else:
                        alive += 1
    return [dead,alive]


def get_edens():
    is_eden = [True for _ in range(size)]





