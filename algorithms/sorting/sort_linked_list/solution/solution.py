class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def sort_ll(self):
        # if head is None, list is sorted.
        if self.head == None:  
            return 
        # set current node to head node
        current = self.head 
        # set index to None
        next_node = None
        # itterate though the linked list
        while(current != None):  
            # next_node will point to node next to current  
            next_node = current.next  
            while(next_node != None):  
                # If current node's data is greater than index's node data, swap the data between them  
                if(current.value > next_node.value):  
                    temp = current.value  
                    current.value = next_node.value 
                    next_node.value = temp  
                next_node = next_node.next  
            current = current.next

n1 = ListNode(5)
n2 = ListNode(6, n1)
n3 = ListNode(4, n2)
n4 = ListNode(1, n3)
llst = LinkedList(n4)

def printlst(lst):
    current = lst.head
    while(current != None):
        print(current.value)
        current = current.next


  
