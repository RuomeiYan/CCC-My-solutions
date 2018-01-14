x = int(input("Enter m: "))
y = int(input("Enter n: "))


def way(m, n):
    if n >= 10:
        return "There are 9 ways to get the sum 10."
    if m > 9:
        m = 9
    n = n+m-9
    if n == 1:
        return "There is 1 way to get the sum 10."
    if n < 0:
        n = 0
    return "There are "+str(n)+" ways to get the sum 10."


if x > y:
    print(way(x,y))
else:
    print(way(y,x))