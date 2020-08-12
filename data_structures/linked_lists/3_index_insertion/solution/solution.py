#Write your answers here 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self, head=None):
        self.head = head
    def insert_at_index(self, index, data):
        start_node = self.head
        if index == 0:
            return Node(data, self.head)
        while index > 1:
            self.head = start_node.next
            index -=1
        start_node.next = Node(data, start_node.next)
        return start_node
        