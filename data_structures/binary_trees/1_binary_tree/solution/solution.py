#Write your solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

left_child = Node(4)
right_child = Node(7)
sample_tree = Node(5, left_child, right_child)