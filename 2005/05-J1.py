print("Number of daytime minutes?")
d = int(input())
print("Number of evening minutes?")
e = int(input())
print("Number of weekend minutes?")
w = int(input())


def cost(dl,dp,ep,wp,d,e,w):
    c = 0
    if d > dl:
        c = dp*(d-dl)
    c += ep*e + wp*w
    return c

a = cost(100,0.25,0.15,0.20,d,e,w)
b = cost(250,0.45,0.35,0.25,d,e,w)
print("Plan A costs %.2f" % a)
print("Plan B costs %.2f" % b)
if abs(a-b) <= 0.001:
    print("Plan A and B are the same price.")
elif a < b:
    print("Plan A is cheapest.")
else:
    print("Plan B is cheapest.")
