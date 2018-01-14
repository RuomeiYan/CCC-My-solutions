import sys
n = int(sys.stdin.readline())
if n < 4:
    print(0)
else:
    print(int((n-1)*(n-2)*(n-3)/6))
