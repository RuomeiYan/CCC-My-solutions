# Wrong program
# Special cases cannot be fixed
# When Bridget is "trapped"!

w = int(input())
h = int(input())
a = int(input())
b = int(input())
s = int(input())
x = a + 1
y = 1
while True:
    if 2*(w+h)-4 <= s:
        s = s-2*(w+h)+5
        y += 1
        w -= 2
        h -= 2
    else:
        break
sx = w-2*a-1
sy = h-2*b-1
while True:
    if sy == 0:
        y += s
        break

    if s > sx-1:   # to the right
        x += sx+1
        s -= sx+1
        print(x,y)
    else:
        x += s
        break
    if s > b:   # downward
        y += b
        s -= b
        print(x,y)
    else:
        y += s
        break
    if s > a:  # to the right
        x += a
        s -= a
        print(x,y)
    else:
        x += s
        break
    if s > sy:  # downward
        y += sy
        s -= sy
        print(x,y)
    else:
        y += s
        break
    if s > a:    # to the left
        x -= a
        s -= a
        print(x,y)
    else:
        x -= s
        break
    if s > b:    # downward
        y += b
        s -= b
        print(x,y)
    else:
        y += s
        break
    if s > sx:    # to the left
        x -= sx
        s -= sx
        print(x,y)
    else:
        x -= s
        break
    if s > b:    # upward
        y -= b
        s -= b
        print("*",x,y)
    else:
        y -= s
        break
    if s > a:    # to the left
        x -= a
        s -= a
        print(x,y)
    else:
        x -= s
        break
    if s > sy:    # upward
        y -= sy
        s -= sy
        print(x,y)
    else:
        y -= s
        break
    if s > a:    # to the right
        x += a
        s -= a
        print(x,y)
        print(s)
    else:
        x += s
        break
    y -= s
    print(x,y)
    break
print(x,y)
print(x)
print(y)


