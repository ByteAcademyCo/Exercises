class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def search(self, x):
        cur_node = self.head
        while(not cur_node == None):
            if cur_node.data == x:
                return True
            cur_node = cur_node.next
        return False
