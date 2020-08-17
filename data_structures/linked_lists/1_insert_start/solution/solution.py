# Write your solution here
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head
    def insert_at_start(self, data):
        Node1 = Node(data)
        Node1.next = self.head
        self.head = Node1
        
