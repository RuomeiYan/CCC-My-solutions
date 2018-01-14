import sys
k = int(sys.stdin.readline())
nums = []
for i in range(k):
    t = int(sys.stdin.readline())
    if t == 0:
        del nums[-1]
    else:
        nums.append(t)
print(sum(nums))
