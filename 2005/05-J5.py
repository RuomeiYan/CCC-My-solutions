def mon_lan(text):
    t = []
    if text == "A":
        return True
    if text == "":
        return False
    for i in range(len(text)):
        if text[i] == "N":
            t.append(mon_lan(text[:i]) and mon_lan(text[i+1:]))
    if text[0] == "B" and text[-1] == "S":
            t.append(mon_lan(text[1:-1]))
    for i in t:
        if i:
            return True

while True:
    word = input()
    if word == "X":
        break
    if mon_lan(word):
        print("YES")
    else:
        print("NO")

