#Write your Answers here
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head
    def insert_at_end(self, data):
        current_node = self.head
        previous_node = self.head
        while not current_node is None:
            previous_node = current_node
            current_node = current_node.next
        new_node = Node(data)
        previous_node.next = new_node