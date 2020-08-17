# Write solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def search(root, key):
    if root is None:
        return False
    elif key == root.key:
        return True
    elif root.key > key:
        return search(root.left, key)
    else:
        return search(root.right, key)