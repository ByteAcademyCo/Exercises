class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def sort_ll(self):
        current_n = self.head
        index = None
        if self.head == None:
            return None
        else:
            while current_n != None:
                index = current_n.next
            while index != None:
                if current_n.value > index.value:
                    x = current_n.value
                    current_n.value = index.value
                    index.value = x
                index = index.next
            current_n = current_n.next