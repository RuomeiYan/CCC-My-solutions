n = int(input())
boxes = [sorted(list(map(int, input().split())), reverse=True) for _ in range(n)]
m = int(input())
items = [sorted(list(map(int, input().split())), reverse=True) for i in range(m)]
boxes.sort(key=lambda x:x[0]*x[1]*x[2])

for j in items:
    for k in boxes:
        if k[0] >= j[0] and k[1] >= j[1] and k[2] >= j[2]:
            print(k[0]*k[1]*k[2])
            break
    else:
        print("Item does not fit.")