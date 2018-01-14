keyboard = {'V': [4, 4], 'R': [3, 6], 'G': [2, 1], 'T': [4, 2],
            'H': [2, 2], 'K': [2, 5], 'D': [1, 4], 'X': [4, 6],
            'A': [1, 1], 'Z': [5, 2], 'Y': [5, 1], ' ': [5, 3],
            'B': [1, 2], '.': [5, 5], '-': [5, 4], 'U': [4, 3],
            'P': [3, 4], 'C': [1, 3], 'Q': [3, 5], 'W': [4, 5],
            'F': [1, 6], 'E': [1, 5], 'I': [2, 3], 'J': [2, 4],
            'M': [3, 1], 'S': [4, 1], 'O': [3, 3], 'N': [3, 2],
            '*': [5, 6], 'L': [2, 6]}


def move(start, end):
    return abs(keyboard[end][0]-keyboard[start][0])+abs(keyboard[end][1]-keyboard[start][1])

text = input()
text += "*"
step = move("A",text[0])
for i in range(len(text)-1):
    step += move(text[i],text[i+1])
print(step)