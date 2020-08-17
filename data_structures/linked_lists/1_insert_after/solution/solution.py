# Write your answers here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class linkedList:
    def __init__(self, head=None):
        self.head = head
    def insert_after_item(self, x, data):
        current_node = self.head
        previous_node = self.head
        new_node = Node(data)
        while current_node:
            if current_node.data == x:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = new_node

# 1 -> 2 -> 3 -> 5
# insert: x=3 data=4

# c_n = 1
# p_n = 1
# n_n = 4

# p_n = c_n = 1
# c_n = 1+next = 2

# p_n = 1+next = 2
# c_n = 2+next = 3

# n_n.next = c_n.next = 5
# 4        ->    5

# c_n.next   =  n_n
# 1 -> 2 -> 3 -> 4 -> 5