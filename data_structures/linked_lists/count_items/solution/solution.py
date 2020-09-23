class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
    
    def get_count(self):
        count = 0
        cur_node = self.head
        while(not cur_node == None):
            count += 1
            cur_node = cur_node.next
        return count