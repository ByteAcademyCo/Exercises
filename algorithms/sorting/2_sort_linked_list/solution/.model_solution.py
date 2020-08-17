class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def sort_ll(self):
        current = self.head 
        index = None
          
        if self.head == None:  
                return 
        else:  
            while(current != None):  
                #Node index will point to node next to current  
                index = current.next  
                  
                while(index != None):  
                    #If current node's data is greater than index's node data, swap the data between them  
                    if(current.value > index.value):  
                        temp = current.value  
                        current.value = index.value 
                        index.value = temp  
                    index = index.next  
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

printlst(llst)
llst.sort_ll()
print(llst.head.next.next.value)

llst.sort_ll()

printlst(llst)


