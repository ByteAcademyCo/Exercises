# Write your solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def Postorder(root):
    lst = []
    if root:
        lst = Postorder(root.left)
        lst += Postorder(root.right)
        lst.append(root.key)
    return lst