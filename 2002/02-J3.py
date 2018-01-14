import sys
PINK = int(input())
GREEN = int(input())
RED = int(input())
ORANGE = int(input())
MONEY = int(input())
counter = 0
minimum = sys.maxsize
for i in range(MONEY//PINK+1):
    for j in range(MONEY//GREEN+1):
        for k in range(MONEY//RED+1):
            for l in range(MONEY//ORANGE+1):
                if i*PINK+j*GREEN+k*RED+l*ORANGE == MONEY:
                    print("# of PINK is %d # of GREEN is %d # of RED is %d # of ORANGE is %d" % (i,j,k,l))
                    counter += 1
                    if i+j+k+l < minimum:
                        minimum = i+j+k+l
print("Total combinations is %d." % (counter))
print("Minimum number of tickets to print is %d." % (minimum))