father = input()
mother = input()
x = int(input())
babies = []
for i in range(x):
    babies.append(input())
baby = []
for i in range(0,10,2):
    if father[i].isupper() and father[i+1].isupper():
        baby.append(father[i])
    elif mother[i].isupper() and mother[i+1].isupper():
        baby.append(mother[i])
    elif father[i].islower() and father[i+1].islower() and mother[i].islower() and mother[i+1].islower():
        baby.append(father[i])
    else:
        baby.append("x")
for i in babies:
    count = 0
    t = True
    for j in i:
        if not(j == baby[count] or baby[count] == "x"):
            t = False
        count += 1
    if t:
        print("Possible baby.")
    else:
        print("Not their baby!")
