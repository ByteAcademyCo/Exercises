class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        cur_node = self.head
        while(cur_node):
            print(cur_node.data)
            cur_node = cur_node.next
