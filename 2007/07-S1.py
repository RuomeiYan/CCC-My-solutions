n = int(input())
for _ in range(n):
    y, m, d = map(int, input().split())
    if y < 1989:
        print("Yes")
        continue
    elif y > 1989:
        print("No")
        continue
    else:
        if m < 2:
            print("Yes")
            continue
        elif m > 2:
            print("No")
            continue
        else:
            if d <= 27:
                print("Yes")
                continue
            else:
                print("No")
                continue