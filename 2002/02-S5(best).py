w = int(input())
h = int(input())
p = int(input())
q = int(input())
m = q / (w - p)
b = -m * p
i = w * 2
count = 0
while True:
    y = m * i + b
    if y % h < 5 or y % h > h - 5:
        if y % h == 0:
            count = i // w + int(y / h) - 2
        else:
            count = i // w + int(y / h) - 1
        break
    if y % h == q:
        count = 0
        break
    i += w
print(count)
