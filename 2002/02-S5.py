w = int(input())
h = int(input())
p = int(input())
q = int(input())
done = False
slope = q / (w - p)
k = 1
while k <= 100000 and not done:
    y = slope * ((k * w) - p)
    x = (k * h) / slope + p
    numh = int((y - (h / 2)) / h) + 1
    numw = int((x - (w / 2)) / w) + 1
    a = numh * h
    b = numw * w
    # print(x, y, numh, numw)
    if abs(a - y) < 5 or abs(b - x) < 5:
        if abs(a - y) < 5:
            if a != y:
                bounce = k - 1 + int(y / h)
            else:
                bounce = k - 1 + int(y / h) - 1
        else:
            if b != x:
                bounce = k - 1 + int(x / w)
            else:
                bounce = k - 1 + int(x / w) - 1
        print(bounce)
        done = True
    k += 1
if not done:
    print(0)
