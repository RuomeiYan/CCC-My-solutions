table = {"CU": "see you", ":-)": "I'm happy", ":-(": "I'm unhappy", ";-)": "wink",
         ":-P": "stick out my tongue", "(~.~)":"sleepy", "TA": "totally awesome",
         "CCC": "Canadian Computing Competition", "CUZ": "because", "TY": "thank-you",
         "YW": "you're welcome", "TTYL": "talk to you later"}
while True:
    phrase = input("Enter phrase> ")
    if phrase in table.keys():
        print(table[phrase])
    else:
        print(phrase)
    if phrase == "TTYL":
        break
