def trident(t, s, h):
    for i in range(t):
        print("*"+" "*s+"*"+" "*s+"*")
    print("*"*(2*s+3))
    for i in range(h):
        print(" "*(s+1)+"*")


t = int(input())
s = int(input())
h = int(input())
trident(t, s, h)
