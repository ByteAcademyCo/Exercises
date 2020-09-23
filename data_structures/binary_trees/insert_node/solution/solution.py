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
        inorder_node_lst = self.inorder_nodes()
        new_node = Node(key)
        for node in inorder_node_lst:
            if not node.left:
                node.left = new_node
                return
            if not node.right:
                node.right = new_node
                return


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.key),
        if self.right:
            self.right.PrintTree()


    # solution #2
    def insert2(self, data):
        # Compare the new value with the parent node
        if self.key:
            if data < self.key:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.key:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.key = data  

items = Node(6)
items.left = Node(11)
items.right = Node(9)
items.left.left = Node(7)
items.right.left = Node(15)
items.right.right = Node(8)

items.insert2(12)
items.PrintTree()


