#Write your solutions here
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

def NthPreorder(root, n):
    preorder_key = Preorder(root)
    if len(preorder_key) > n:
        return preorder_key[n-1]
    else:
        return f'no {n}-th element'