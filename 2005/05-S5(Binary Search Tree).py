# Binary Search Tree
import sys


class Node:
    """
    score and rank are integers.
    left and right are nodes
    """
    def __init__(self, s):
        # The "rank" here means how many leaves are in the right subtree, not literally the ranking
        self.score = s
        self.rank = 0
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add_(self, s):
        rank = 0
        if self.root is None:
            self.root = Node(s)
        else:
            n = self.root
            while True:
                if s < n.score:
                    rank += n.rank + 1
                    if n.left is None:
                        n.left = Node(s)
                        return rank
                    else:
                        n = n.left
                else:
                    n.rank += 1
                    if n.right is None:
                        n.right = Node(s)
                        return rank
                    else:
                        n = n.right
        return rank

t = int(sys.stdin.readline())
x = Tree()
sum_ = 0
for k in range(t):
    sum_ += x.add_(int(sys.stdin.readline()))
ans = sum_ / t + 1
print("%.2f" % ans)
