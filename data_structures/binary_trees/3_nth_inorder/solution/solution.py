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
def NthInorder(root, n):
    inorder_key = Inorder(root)
    if len(inorder_key) > n:
        return inorder_key[n-1]
    else:
        return f'no {n}-th element'