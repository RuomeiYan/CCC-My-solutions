reactions = [["AA", "B", "DD"], ["A", "B", "C", "D"], ["CC", "D"], ["BBB"], ["A", "D"]]
n = int(input())
cases = []
for i in range(n):
    matter = input().split()
    for j in range(4):
        matter[j] = int(matter[j])
    cases.append("A"*matter[0]+"B"*matter[1]+"C"*matter[2]+"D"*matter[3])


def is_in(a,b):
    for i in a:
        if i not in b:
            return False
    return True


def react(a,b):
    for i in a:
        b = b.replace(i, "", 1)
    return b


# True means the current player will lose the game; while False means winning
def function(left):
    for i in reactions:
        if is_in(i,left) and function(react(i,left)):
                return False
    return True

for i in cases:
    if function(i):
        print("Roland")
    else:
        print("Patrick")
