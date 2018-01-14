w, h = map(int, input().split())
cx = 0
cy = 0
while True:
    x, y = map(int, input().split())
    if x == y == 0:
        break
    cx += x
    cy += y
    if cx < 0:
        cx = 0
    elif cx > w:
        cx = w
    if cy < 0:
        cy = 0
    elif cy > h:
        cy = h
    print(cx, cy)
