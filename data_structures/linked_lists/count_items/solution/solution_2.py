class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
        #self.counter = 0
        
    def get_count(self):
        temp = self.head
        count = 0
        while(not temp == None):
            count += 1
            temp = temp.next
        return count    

#def push(self, new_data):
    #new_node = Node(new_data)
    #new_node.next = self.headself.head = new_node
    
#def printList(self):
    #temp = self.head
    #while(temp):
        #print(temp.data)
        #temp = temp.next    

#def get_count(self, temp, key):
    #if temp is None:
        #return 0
    #if temp.data == key:
        #return 1 + get_count(temp.next, key)
    #return get_count(temp.next, key)


