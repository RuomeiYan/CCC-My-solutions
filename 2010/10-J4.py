# To check if the sequence has a period of n
def verify(seq, n):
    for i in range(n, len(seq)):
        if seq[i] != seq[i % n]:
            return False
    return True

while True:
    # Input data, only stores "changes" in a list named "seq"
    seq = input().split()
    if seq[0] == "0":
        break
    seq = seq[1:]
    for i in range(len(seq)-1):
        seq[i] = int(seq[i+1]) - int(seq[i])
    seq.pop()

    # Determine the shortest cycle
    t = len(seq)
    for i in range(1,len(seq)):
        if seq[0] == seq[i] and verify(seq,i):
            t = min(t, i)
            break
    print(t)