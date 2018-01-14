print("Welcome to Chip's Fast Food Emporium")
a = int(input("Please enter a burger choice: "))
b = int(input("Please enter a side order choice: "))
c = int(input("Please enter a drink choice: "))
d = int(input("Please enter a dessert choice: "))

if a == 1: ca = 461
elif a == 2: ca = 431
elif a == 3: ca = 420
else: ca = 0

if b == 1: ca += 100
elif b == 2: ca += 57
elif b == 3: ca += 70

if c == 1: ca += 130
elif c == 2: ca += 160
elif c == 3: ca += 118

if d == 1: ca += 167
elif d == 2: ca += 266
elif d == 3: ca += 75

print("Your total Calorie count is %d." % ca)
