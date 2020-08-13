class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key


def Inorder(root):
    if not root:
        return []
    return Inorder(root.left) + [root.key] + Inorder(root.right)

def NthInorder(root, n):
    inorder_keys = Inorder(root)
    if len(inorder_keys) > n:
        return inorder_keys[n-1]
    else:
        return f'no {n}-th element'


items = Node(6)
items.left = Node(4)
items.right = Node(7)
items.left.left = Node(3)
items.left.right = Node(5)
print(Inorder(items))
print(NthInorder(items, 6))