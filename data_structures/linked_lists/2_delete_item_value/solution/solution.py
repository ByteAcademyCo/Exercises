# Write your solution here
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head
    def delete_item_by_value(self, x):
        current_node = self.head
        previous_node = current_node
        while(not current_node is None and not current_node.data is x):
            previous_node = current_node
            current_node = current_node.next
        if not current_node is None:
            previous_node.next = current_node.next