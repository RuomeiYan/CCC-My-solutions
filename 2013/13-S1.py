import sys
n = int(sys.stdin.readline())
sign = True
while sign:
    n += 1
    t = str(n)
    for i in t:
        if t.count(i) > 1:
            break
    else:
        print(n)
        sign = False
