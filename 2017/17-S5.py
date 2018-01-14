import sys
from collections import defaultdict
import copy
n, m, q = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
nums = [0] + list(map(int, sys.stdin.readline().split()))
lines = defaultdict(list)
for i in range(n):
    lines[a[i]].append(i+1)


def move(line, t):
    op = lines[line]
    t %= len(op)
    if t <= 3:
        for _ in range(t):
            q = nums[op[-1]]
            for i in range(len(op)-1, 0, -1):
                nums[op[i]] = nums[op[i-1]]
            nums[op[0]] = q
    else:
        nums_copy = copy.deepcopy(nums)
        for i in range(len(op)):
            nums[op[i]] = nums_copy[op[i-t]]

operations = defaultdict(int)
for _ in range(q):
    b = list(map(int, sys.stdin.readline().split()))
    if b[0] == 2:
        operations[b[1]] += 1
    elif b[0] == 1:
        for i in operations.keys():
            move(i, operations[i])
        print(sum(nums[b[1]: b[2]+1]))
        operations = defaultdict(int)
