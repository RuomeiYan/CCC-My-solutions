# Copy from mmhs.ca/ccc/index.htm
STREET_LEN = 1000000


def hydrants(hose, houses):
    best = len(houses)
    diam = hose * 2
    i = 0
    while i < len(houses) and houses[i] <= houses[0] + diam:
        count = 1
        curEnd = houses[i]
        j = i + 1
        while j < len(houses) and houses[i] > houses[j] + diam - STREET_LEN:
            if houses[j] > curEnd:
                count += 1
                curEnd = houses[j] + diam
            j = j + 1
        best = min(best, count)
        i = i + 1
    return best


# A standard binary search of the hose lengths
# does the trick.

h = int(input())
houses = []
for i in range(h):
    houses.append(int(input()))
houses.sort()
k = int(input())
lo = -1
hi = STREET_LEN
while (hi > (lo+1)):
    mid = (lo + hi) // 2
    if (hydrants(mid, houses) > k):
        lo = mid
    else:
        hi = mid
print(hi)