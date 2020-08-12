#Write your answers here 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self, head=None):
        self.head = head
    def insert_at_index(self, index, data):
        current_index = 1
        current_node = self.head
        while current_index < index-1:
            current_node = current_node.next
            current_index +=1
        next_node = current_node.next
        new_node = Node(data)
        new_node.next = next_node
        current_node.next = new_node