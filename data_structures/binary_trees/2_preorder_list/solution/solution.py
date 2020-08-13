# Write your solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
def Preorder(root):
    lst = []
    if root:
        lst.append(root.key)
        lst += Preorder(root.left)
        lst += Preorder(root.right)
    return lst