cases = [0,100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
unfold = int(input())
for i in range(unfold):
    cases[int(input())] = 0
total = 0
for i in cases:
    total += i
offer = int(input())
if offer * (10-unfold) > total:
    print("deal")
else:
    print("no deal")