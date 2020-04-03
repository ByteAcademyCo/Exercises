# A Binary Tree (BT) is either:
# None
# Node

class Node:
    # val: int
    # left: BT
    # right: BT
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

# Write a function called length that consumes a Binary Tree t and returns how many Nodes are in t
def length(t):
    if t == None:
        return 0
    return 1 + length(t.left) + length(t.right)

def test_length():
    t = Node(1, Node(2, Node(3, None, None), None), Node(4, None, None))
    assert length(t) == 4
