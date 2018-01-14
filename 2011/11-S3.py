import sys
for _ in range(int(sys.stdin.readline())):
    m, x, y = map(int, sys.stdin.readline().split())
    m -= 1
    x /= 5 ** m
    y /= 5 ** m
    while m >= 0:
        x = round(x, 5)
        y = round(y, 5)
        m -= 1
        if 1 <= x < 2:
            if y < 1:
                print("crystal")
                break
            elif m >= 0 and y < 5/3:
                x = (x - 1) * 5
                y = (y - 1) * 5
                continue
            else:
                print("empty")
                break
        elif 2 <= x < 3:
            if y < 2:
                print("crystal")
                break
            elif m >= 0 and y < 8/3:
                x = (x - 2) * 5
                y = (y - 2) * 5
                continue
            else:
                print("empty")
                break
        elif 3 <= x < 4:
            if y < 1:
                print("crystal")
                break
            elif m >= 0 and y < 5/3:
                x = (x - 3) * 5
                y = (y - 1) * 5
                continue
            else:
                print("empty")
                break
        else:
            print("empty")
            break
