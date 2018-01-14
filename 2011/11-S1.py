import sys
n = int(sys.stdin.readline())
t = 0
s = 0
for _ in range(n):
    text = sys.stdin.readline()
    t += text.count('T') + text.count('t')
    s += text.count('S') + text.count('s')
if s >= t:
    print('French')
else:
    print('English')

