text = input()
n = {"A":0, "B":0}
while text[0] != "7":
    if text[0] == "1":
        n[text[2]] = int(text[3:])
    elif text[0] == "2":
        print(n[text[2]])
    elif text[0] == "3":
        n[text[2]] += n[text[4]]
    elif text[0] == "4":
        n[text[2]] *= n[text[4]]
    elif text[0] == "5":
        n[text[2]] -= n[text[4]]
    elif text[0] == "6":
        n[text[2]] = int(n[text[2]]/n[text[4]])
    text = input()