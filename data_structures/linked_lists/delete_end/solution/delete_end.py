class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self, head=None):
        self.head = head
        
    #   def push(head, data):
    #     if not head:
    #         return Node(data)
    #     temp = Node(data)
    #     temp.next = head
    #     head = temp
    #     return head 
    
    def delete_at_end(self):
        if self.head == None:
            return None
        # if self.head.next == None:
        #     head = None
        #     return None
        second_last = self.head
        while(second_last.next.next is not None):
            second_last = second_last.next
        second_last.next = None
        return second_last