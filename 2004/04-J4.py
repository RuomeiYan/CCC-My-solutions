key = input()
text = input()
word = []
for i in text:
    if i.isalpha():
        word.append(i)
for i in range(len(word)):
    a = ord(word[i]) + ord(key[i % len(key)]) - ord("A")
    if a > ord("Z"):
        a -= 26
    print(chr(a),end="")
