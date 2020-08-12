# Write your solution here
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head
    def delete_item_by_value(self, x):
        current_node = self.head
        previous_node = self.head
        while current_node:
            if current_node.data == x:
                next_node = current_node.next
                previous_node.next = next_node
                return
            previous_node = current_node
            current_node = current_node.next
        return 
# 1 -> 2 -> 3 -> 4
# 1 -> 2 -> 4
# delete: 3

# c_n = 1
# p_n = 1

# p_n = 1
# c_n = 1+next = 2

# p_n = 2
# c_n = 2+next = 3

# n_n = c_n + next = 4
# p_n.next = 4
