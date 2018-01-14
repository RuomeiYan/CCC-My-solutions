constraints = [("1","7"), ("1","4"), ("2","1"), ("3","4"), ("3","5")]
while True:
    constraints.append((input(),input()))
    if constraints[-1] == ("0","0"):
        constraints.remove(("0","0"))
        break
for i in range(2134567,6754322):
    if 4000000 <= i <= 6000000:
        continue
    i = str(i)
    if ("1" in i) and ("2" in i) and ("3" in i) and ("4" in i) and ("5" in i) and ("6" in i) and ("7" in i):
        if i == "6754321":
            print("Cannot complete these tasks. Going to bed.")
            break
        sign = False
        for j in constraints:
            if i.index(j[0]) > i.index(j[1]):
                sign = True
                break
        if sign:
            continue
        for k in i:
            print(k,end=" ")
        break
    else:
        continue