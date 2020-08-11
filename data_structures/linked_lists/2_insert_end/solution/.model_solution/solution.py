class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, data):
        cur_node = self.head
        prev_node = cur_node
        while(not cur_node == None):
            prev_node = cur_node
            cur_node = cur_node.next
        new_node = Node(data)
        prev_node.next = new_node
