t = int(input())
keyboard = {"ABC":2, "DEF":3, "GHI":4, "JKL":5, "MNO":6, "PQRS":7, "TUV":8, "WXYZ":9}
numbers = []
for _ in range(t):
    numbers.append(input())
    numbers[-1] = numbers[-1].replace("-", "")
for i in range(t):
    temp = ""
    for j in range(10):
        if numbers[i][j].isdigit():
            temp += numbers[i][j]
        else:
            for k in keyboard.keys():
                if numbers[i][j] in k:
                    temp += str(keyboard[k])
                    break
    numbers[i] = temp
for i in numbers:
    print(i[:3] + "-" + i[3:6] + "-" + i[6:])

