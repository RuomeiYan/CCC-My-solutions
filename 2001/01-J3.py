hand = input()


def output(suit):
    string = ""
    for i in suit:
        string = string + i + " "
    return string


def points(suit):
    point = 0
    for i in suit:
        if i == "A":
            point += 4
        elif i == "K":
            point += 3
        elif i == "Q":
            point += 2
        elif i == "J":
            point += 1
    if len(suit) == 0:
        point += 3
    elif len(suit) == 1:
        point += 2
    elif len(suit) == 2:
        point += 1
    return str(point)

clubs = hand[hand.index("C")+1:hand.index("D")]
diamonds = hand[hand.index("D")+1:hand.index("H")]
hearts = hand[hand.index("H")+1:hand.index("S")]
spades = hand[hand.index("S")+1:len(hand)]
print("%11s%29s" % ("Cards Dealt", "Points"))
t = "Clubs "+output(clubs)
print(t+" "*(40-len(t)-len(points(clubs)))+points(clubs))
t = "Diamonds "+output(diamonds)
print(t+" "*(40-len(t)-len(points(diamonds)))+points(diamonds))
t = "Hearts "+output(hearts)
print(t+" "*(40-len(t)-len(points(hearts)))+points(hearts))
t = "Spades "+output(spades)
print(t+" "*(40-len(t)-len(points(spades)))+points(spades))
total = int(points(clubs)) + int(points(diamonds)) + int(points(hearts)) + int(points(spades))
print("%40s" % ("Total "+str(total)))
