#Write your solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
def Inorder(root):
    lst = []
    if root:
        lst = Inorder(root.left)
        lst.append(root.key)
        lst += Inorder(root.right)
    return lst