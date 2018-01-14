def is_operator(x):
    return x == "+" or x == "-"


def output(x):
    for i in x:
        if type(i) == list:
            output(i)
        else:
            print(i,end=" ")

prefix = input()
while prefix != "0":
    prefix = prefix.split()
    while True:
        for i in range(len(prefix)-2):
            if is_operator(prefix[i]) and (not is_operator(prefix[i+1])) and (not is_operator(prefix[i+2])):
                prefix[i] = [prefix[i+1], prefix[i+2], prefix[i]]
                prefix = prefix[:i+1] + prefix[i+3:]
                break
        else:
            output(prefix)
            print()
            break
    prefix = input()