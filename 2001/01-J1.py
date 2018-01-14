n = int(input())
for i in range(1,int(n/2)+2):
    print("*"*(i*2-1)+" "*(2*n-4*i+2)+"*"*(i*2-1))
for i in range(int(n/2),0,-1):
    print("*"*(i*2-1)+" "*(2*n-4*i+2)+"*"*(i*2-1))

