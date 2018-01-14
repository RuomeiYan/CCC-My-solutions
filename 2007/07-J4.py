a = input("Enter first phrase> ")
b = input("Enter second phrase> ")
a = sorted(list("".join(a.split())))
b = sorted(list("".join(b.split())))
if a == b:
    print("Is an anagram.")
else:
    print("Is not an anagram.")