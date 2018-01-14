n = int(input())


def is_fix(x, y):
    if x == y[-len(x):] or x == y[:len(x)]:
        return True
    return False

for _ in range(n):
    a = input()
    b = input()
    c = input()
    t = []
    if len(a) > len(b):
        t.append(is_fix(b, a))
    else:
        t.append(is_fix(a, b))
    if len(b) > len(c):
        t.append(is_fix(c, b))
    else:
        t.append(is_fix(b, c))
    if len(c) > len(a):
        t.append(is_fix(a, c))
    else:
        t.append(is_fix(c, a))
    if True in t:
        print("No")
    else:
        print("Yes")

