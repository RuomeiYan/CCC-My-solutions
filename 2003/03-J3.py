s = 1
d = int(input())
while d != 0:
    if s + d == 100:
        print("You are now on square 100")
        print("You Win!")
        break
    elif s + d > 100:
        print("You are now on square",s)
        d = int(input())
    else:
        s += d
        if s == 54: s = 19
        elif s == 90: s = 48
        elif s == 99: s = 77
        elif s == 9: s = 34
        elif s == 40: s = 64
        elif s == 67: s = 86
        print("You are now on square",s)
        d = int(input())
if d == 0:
    print("You Quit!")
