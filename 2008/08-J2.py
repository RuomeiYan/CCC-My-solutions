songs = ["A", "B", "C", "D", "E"]
while True:
    b = int(input("Button number: "))
    n = int(input("Number of presses: "))
    if b == 1:
        n %= 5
        songs = songs[n:]+ songs[:n]
    elif b == 2:
        n %= 5
        songs = songs[-n:] + songs[:-n]
    elif b == 3:
        if n % 2 == 1:
            songs[0], songs[1] = songs[1],songs[0]
    else:
        for i in songs:
            print(i,end=" ")
        break