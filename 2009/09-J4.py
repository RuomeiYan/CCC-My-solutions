text = ["WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY"]
w = int(input("Enter w: "))
while text:
    t = []
    s = []
    l = w+1
    # Put the maximum amount of words into the current line
    while text and len(text[0]) < l:
        t.append(text[0])
        s.append(".")
        l -= len(text[0])+1
        text = text[1:]
    if len(t) > 1: # If there are more than one word in that line
        s.pop()  # Get rid of the last "."
        while l > 0:        # Put extra spaces(".") in it
            for i in range(len(s)):
                s[i] += "."
                l -= 1
                if l == 0:
                    break
        for i in range(len(t)-1):  # Output this line
            print(t[i]+s[i],end="")
        print(t[-1])
    else:  # If there is only one word in that line
        print(t[0]+"."*l)







