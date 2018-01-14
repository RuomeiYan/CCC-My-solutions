def verify(x):
    if 0 <= x <= 2359:
        return x
    elif x < 0:
        return x+2400
    else:
        return x-2400
ottawa = int(input())
print(ottawa,"in Ottawa")
print(verify(ottawa-300),"in Victoria")
print(verify(ottawa-200),"in Edmonton")
print(verify(ottawa-100),"in Winnipeg")
print(ottawa,"in Toronto")
print(verify(ottawa+100),"in Halifax")
if ottawa % 100 > 29:
    print(verify(ottawa+170),"in St. John's")
else:
    print(verify(ottawa+130),"in St. John's")