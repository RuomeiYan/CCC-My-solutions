import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = [int(sys.stdin.readline()) for t in range(n)]
    a.reverse()
    c = 1
    b = []
    for i in a:
        while b:
            if b[-1] == c:
                c += 1
                del b[-1]
            else:
                break
        if i == c:
            c += 1
        else:
            if not b or i < b[-1]:
                b.append(i)
            else:
                print('N')
                break
    else:
        print('Y')






