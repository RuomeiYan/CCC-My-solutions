import sys
import itertools


def all_pos(x, y):
    pos = []
    if x + y not in pos:
        pos.append(x + y)
    if x - y > 0 and x - y not in pos:
        pos.append(x - y)
    if x * y not in pos:
        pos.append(x * y)
    if y != 0 and x % y == 0 and x // y not in pos:
        pos.append(x // y)
    return pos

for _ in range(int(sys.stdin.readline())):
    cards = [int(sys.stdin.readline()) for t in range(4)]
    indices = [0, 1, 2, 3]
    pos2 = []
    for i in itertools.permutations(indices):
        pos = []
        for j in all_pos(cards[i[0]], cards[i[1]]):
            pos += all_pos(j, cards[i[2]])
        for k in pos:
            pos2 += all_pos(k, cards[i[3]])
    for i in itertools.combinations(indices, 2):
        indices_set = set(indices)
        sec_pair = tuple(indices_set - set(i))
        for i in all_pos(cards[i[0]], cards[i[1]]):
            for j in all_pos(cards[sec_pair[0]], cards[sec_pair[1]]):
                pos2 += all_pos(i, j)
    for i in range(24, -1, -1):
        if i in pos2:
            print(i)
            break
