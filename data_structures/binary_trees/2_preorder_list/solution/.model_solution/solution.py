# Write your solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key

def Preorder(root):
    if not root:
        return []
    return [root.key] + Preorder(root.left) + Preorder(root.right)

items = Node(6)
items.left = Node(4)
items.right = Node(7)
items.left.left = Node(3)
items.left.right = Node(5)
print(Preorder(items))