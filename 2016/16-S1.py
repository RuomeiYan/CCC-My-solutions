import sys
a = sorted(list(sys.stdin.readline().strip()), reverse=True)
b = sorted(list(sys.stdin.readline().strip()), reverse=True)
if len(a) != len(b):
    print('N')
elif '*' not in b:
    if a == b:
        print('A')
    else:
        print('N')
else:
    c = 0
    for i in range(len(a)):
        if a[i] != b[i-c]:
            c += 1
    if b[-c] == '*':
        print('A')
    else:
        print('N')





