class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
        
    def get_count(self):
        count = 0
        temp = self.head
        while(not temp == None):
            count += 1
            temp = temp.next
        return count