class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
    
    def delete_item_by_value(self, x):
        items = self.head
        prev_node = items
        while(not items == None and not items.data == x):
            prev_node = items
            items = items.next
        if not items == None:
            prev_node.next = items.next
        return