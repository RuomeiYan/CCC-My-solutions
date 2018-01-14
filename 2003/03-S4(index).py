# TLE
n = int(input())
for _ in range(n):
    st = input()
    count = 1
    for i in range(len(st)):
        for j in range(i+1, len(st)+1):
            if st.index(st[i:j]) == i:
                count += 1
    print(count)
