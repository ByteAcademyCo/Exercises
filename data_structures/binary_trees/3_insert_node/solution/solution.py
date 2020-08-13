#Write your solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
    
    # Fill in your code here
    def insert(self, key):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            else:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insert(key)
        else:
            self.key = key