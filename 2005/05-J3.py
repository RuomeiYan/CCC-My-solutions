ins = []
ins.append(input())
while ins[-1] != "SCHOOL":
    ins.append(input())
ins.reverse()
for i in range(1,len(ins)-1,2):
    if ins[i] == "L":
        print("Turn RIGHT onto",ins[i+1],"street.")
    else:
        print("Turn LEFT onto",ins[i+1],"street.")
if ins[-1] == "L":
    print("Turn RIGHT into your HOME.")
else:
    print("Turn LEFT into your HOME.")