#Write your solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
    
    # Fill in your code here
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