class Node:
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None

def tree_max(node):
    if not node:
        return float("-inf")
    maxleft  = tree_max(node.left)
    maxright = tree_max(node.right)
    return max(node.key, maxleft, maxright)

def tree_min(node):
    if not node:
        return float("inf")
    minleft  = tree_min(node.left)
    minright = tree_min(node.right)
    return min(node.key, minleft, minright)

def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
        verify(node.left) and verify(node.right)):
        return 1 # Vaild
    else:
        return 0 # Invalid

# root = Node(2,"Two")  
# root.left = Node(1,"one")  
# root.right = Node(3,"Three") 


root = Node(1,"one")  
root.left = Node(2,"Two")  
root.right = Node(3,"Three") 
result = verify(root)
print(result)
