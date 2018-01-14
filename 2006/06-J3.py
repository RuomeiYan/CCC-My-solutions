keyboard = {"adgjmptw":1, "behknqux":2, "cfilorvy":3, "sz":4}
key = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
while True:
    word = input()
    if word == "halt":
        break
    p = "."
    r = 0
    for i in word:
        for j in keyboard.keys():
            if i in j:
                r += keyboard[j]
        for j in key:
            if p in j and i in j:
                r += 2
        p = i
    print(r)