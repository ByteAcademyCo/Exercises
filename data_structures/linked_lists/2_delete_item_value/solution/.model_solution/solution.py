class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def delete_item_by_value(self, x):
        cur_node = self.head
        prev_node = cur_node
        while(not cur_node == None and not cur_node.data == x):
            prev_node = cur_node
            cur_node = cur_node.next
        if not cur_node == None:
            prev_node.next = cur_node.next
