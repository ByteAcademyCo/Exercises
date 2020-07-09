class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)



# # A utility function to search a given key in BST 
def search(root,key): 
      
    # Base Cases: root is null or key is present at root 
    if root is None :
        return False
    elif root.data == key:
        return True
    
    # Key is greater than root's key 
    if root.data < key: 
        return search(root.right,key) 
    
    # Key is smaller than root's key 
    return search(root.left,key)

result = search(root,15)
print(result)


