x={}
for i in range(int(input())):
     y=input().split()
     x[y[1]]=y[0]
code=''
for i in input():
     code+=i
     if code in x:
          print(x[code],end='')
          code=''


