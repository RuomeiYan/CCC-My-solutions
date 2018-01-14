import math
c = int(input())
while c != 0:
    for i in range(math.floor(math.sqrt(c)),0,-1):
        if c % i == 0:
            j = c // i
            print("Minimum perimeter is",2*(i+j),"with dimensions",i,"x",j)
            break
    c = int(input())

