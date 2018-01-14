def syllable(line):
    line = line.lower()
    word = line.split()[-1]
    for i in range(len(word)-1,-1,-1):
        if word[i] in "aeiou":
            return word[i:]
    return word

for i in range(int(input())):
    a1 = syllable(input())
    a2 = syllable(input())
    a3 = syllable(input())
    a4 = syllable(input())
    if a1 == a2 == a3 == a4:
        print("perfect")
    elif a1 == a2 and a3 == a4:
        print("even")
    elif a1 == a3 and a2 == a4:
        print("cross")
    elif a1 == a4 and a2 == a3:
        print("shell")
    else:
        print("free")