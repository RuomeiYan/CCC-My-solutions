def is_consonant(char):
    char = char.lower()
    return not (char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "y")

word = input()
while word != "quit!":
    if len(word) > 4 and is_consonant(word[-3]) and word[-2:] == "or":
        word = word[:-2] + "our"
    print(word)
    word = input()


