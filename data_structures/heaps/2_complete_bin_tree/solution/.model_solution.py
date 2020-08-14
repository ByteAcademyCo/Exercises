class Tree:
  def __init__(self, root_node=None):
      self.root_node = root_node

class TreeNode:
  def __init__(self, value, left=None, right=None):
      self.value = value
      self.left = left
      self.right = right

    

# Fill in your code here
def is_complete(tree):
    return is_complete_node(tree.root_node)

def is_complete_node(treeNode):
    if not treeNode:
        return True
    elif not treeNode.left and not treeNode.right:
        return True
    elif treeNode.left and treeNode.right:
        return is_complete_node(treeNode.left) and is_complete_node(treeNode.right)
    elif treeNode.left:
        return is_complete_node(treeNode.left)
    elif treeNode.right:
        return False
    else:
        return False

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3, n1, n2)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6, n4, n5)
n7 = TreeNode(7, n3, n6)
tree = Tree(n7)

print(is_complete(tree))   