import sys
limit = int(sys.stdin.readline())
n = int(sys.stdin.readline())
bridge = []
if n == 0:
    print(0)
elif n <= 4:
    for i in range(n):
        bridge.append(int(sys.stdin.readline()))
    for i in range(1, n+1):
        if sum(bridge[:i]) > limit:
            print(i - 1)
            break
    else:
        print(n)
else:
    for i in range(4):
        bridge.append(int(sys.stdin.readline()))
    for i in range(1, 5):
        if sum(bridge[:i]) > limit:
            print(i - 1)
            break
    else:
        t = 4
        while t < n:
            bridge.pop(0)
            bridge.append(int(sys.stdin.readline()))
            if sum(bridge) > limit:
                print(t)
                break
            t += 1
        else:
            print(n)
