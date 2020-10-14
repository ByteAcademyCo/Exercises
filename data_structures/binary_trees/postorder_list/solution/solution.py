class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key

def Postorder(root):
    if not root:
        return []
    return Postorder(root.left) + Postorder(root.right) + [root.key]

items = Node(6)
items.left = Node(4)
items.right = Node(7)
items.left.left = Node(3)
items.left.right = Node(5)
print(Postorder(items))