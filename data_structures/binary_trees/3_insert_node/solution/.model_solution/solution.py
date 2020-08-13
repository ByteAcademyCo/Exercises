#Write your solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key

    
    def inorder_nodes(self):
        if not self:
            return []
        leftNodes = self.left.inorder_nodes() if self.left else []
        rightNodes = self.right.inorder_nodes() if self.right else []
        return [self] + leftNodes + rightNodes


    def insert(self, key):
        if not self: 
            return Node(key)
        node_lst = self.inorder_nodes()
        for node in node_lst:
            if not node.left:
                node.left = Node(key)
                return
            elif not node.right:
                node.right = Node(key)
                return
        return

items = Node(6)
items.left = Node(11)
items.right = Node(9)
items.left.left = Node(7)
items.right.left = Node(15)
items.right.right = Node(8)
items.insert(12)

def Inorder_keys(root):
        if not root:
            return []
        return Inorder_keys(root.left) + [root.key] + Inorder_keys(root.right)

print(Inorder_keys(items))