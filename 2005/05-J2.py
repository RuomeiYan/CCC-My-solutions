print("Enter lower limit of range")
l = int(input())
print("Enter upper limit of range")
u = int(input())
n = 0
for i in range(l,u+1):
    count = 0
    for j in range(2,i):
        if i % j == 0:
            count += 1
    if count == 2:
        n += 1
print("The number of RSA numbers between",l,"and",u,"is",n)