# Write your answers here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class linkedList:
    def __init__(self, head=None):
        self.head = head
    def insert_after_item(self, x, data):
        current_node = self.head
        previous_node = self.head
        if current_node is None:
            new_node = Node(data)
            self.head = new_node
            return
        while(not current_node is None and current_node.data is not x):
            previous_node = current_node
            current_node = current_node.next
        new_node = Node(data)
        if current_node is None:
            previous_node.next = new_node
        else:
            _next = current_node.next
            current_node.next = new_node
            new_node.next = _next