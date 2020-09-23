class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_index(self, index, data):
        cur_idx = 1
        cur_node = self.head
        prev_node = cur_node
        new_node = Node(data)

        while(cur_idx < index):
            prev_node = cur_node
            cur_node = cur_node.next
            cur_idx += 1
        new_node.next = cur_node
        prev_node.next = new_node


