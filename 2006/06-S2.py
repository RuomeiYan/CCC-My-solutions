plain = input()
cipher = input()
encrypted = input()
tran = {}
for i in range(len(plain)):
    if "A" <= cipher[i] <= "Z" or cipher[i] == " ":
        tran[cipher[i]] = plain[i]
for i in encrypted:
    if i in tran.keys():
        print(tran[i], end="")
    else:
        print(".", end="")
