a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
Nikky = (a-b)*(s//(a+b))
Byron = (c-d)*(s//(c+d))

if s%(a+b) <= a:
    Nikky += s%(a+b)
else:
    Nikky += 2*a-s%(a+b)

if s%(c+d) <= c:
    Byron += s%(c+d)
else:
    Byron += 2*c-s%(c+d)

if Byron > Nikky:
    print("Byron")
elif Byron < Nikky:
    print("Nikky")
else:
    print("Tied")
