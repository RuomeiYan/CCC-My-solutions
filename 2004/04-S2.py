n, k = map(int, input().split())
rounds = []
rank = []
score = []


# function to update the rank
def update_rank(score):
    global rank
    mark = sorted(score,reverse=True)
    for t in range(n):
        rank[t] = max(mark.index(score[t]), rank[t])
# Input data
for i in range(k):
    rounds.append([])
    for j in input().split():
        rounds[i].append(int(j))
# Initialization
for i in range(n):
    score.append(0)
    rank.append(0)
# Main program
for i in rounds:
    for j in range(n):
        score[j] += i[j]
    update_rank(score)
# Output data
top_score = max(score)
for i in range(n):
    if score[i] == top_score:
        print("Yodeller %d is the TopYodeller: score %d, worst rank %d" % (i+1,top_score,rank[i]+1))



