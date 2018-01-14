a=[tuple([2, 1, 0, 2]), tuple([1, 1, 1, 1]), tuple([0, 0, 2, 1]), tuple([0, 3, 0, 0]), tuple([1, 0, 0, 1])]
d={}


def thinginator(l, i):
    s=l[0]-a[i][0]
    t=l[1]-a[i][1]
    u=l[2]-a[i][2]
    v=l[3]-a[i][3]
    return [bool(s>=0 and t>=0 and u>=0 and v>=0), tuple([s, t, u, v])]


def nuke(r):  # Return False if it is a winning position; Return True if it is a losing position
    if r in d:   # If it is in the record, just return the stored value
        return not d[r]
    else:
        d[r]=False     # Assume it is a losing position
        for k in range(0, 5):
            temp=thinginator(r, k)   # Try every possible reaction
            if temp[0]:   # If it doesn't reach a losing position
                d[r]=nuke(temp[1])   # After this reaction... Return it is a winning position or losing position
            if d[r]==True:  # If the current position is a winning position
                return not d[r]   # Return False, winning!
        print(d)
        print(d[r])
    return not d[r]  # return the opposite boolean value

h=int(input())
for butt in range(0, h):
    if nuke(tuple([int(x) for x in input().split()])) is False:
        print("Patrick")
    else:
        print("Roland")
