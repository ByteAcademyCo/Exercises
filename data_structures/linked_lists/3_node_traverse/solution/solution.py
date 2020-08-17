# Write your answers here
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self, head=None):
        self.head = head
    def traverse(self):
        current_node = self.head
        while not current_node is None:
            print(current_node.data)
            current_node = current_node.next