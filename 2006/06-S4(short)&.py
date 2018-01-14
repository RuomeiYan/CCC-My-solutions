from itertools import product


def is_gp(gp):
    print(list(tuple(x[i] for i in x) for x in gp))
    print(list(product(gp, repeat=2)))
    # 1st line: if there is an identity in the group (one line equals to [1, 2, 3, .. ,n])
    # 2nd line: no repeated element in each line
    # 3rd line: if x and y are in G, x * y is in G
    # 4th line: associativity
    return tuple(range(len(gp))) in gp and\
           all(len(x) == len(set(x)) for x in gp) and\
           all(tuple(x[i] for i in x) in gp for x in gp) and\
           all(tuple(y[i] for i in x) in gp
               for (x, y) in product(gp, repeat=2))

for n in iter(input, '0'):
    gp = [tuple(int(i)-1 for i in input().split()) for _ in range(int(n))]
    print(gp)
    print('yes' if is_gp(gp) else 'no')
