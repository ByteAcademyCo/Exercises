class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def enqueue(self, value):
        new_node = ListNode(value)
        if not self.tail_node:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next = new_node
            self.tail_node = new_node

    def dequeue(self):
        if not self.head_node:
            raise IndexError
        value = self.head_node.value
        self.head_node = self.head_node.next
        if not self.head_node:
            self.tail_node = None
        return value

    # You may want to solve this magic method first!
    def __len__(self):
        current_node = self.head_node
        number_nodes = 0
        while current_node:
            number_nodes += 1
            current_node = current_node.next
        return number_nodes

    # Fill in the code for __len__
    def __eq__(self, other):
        #return len(self) == len(other)
        if len(self) == len(other):
            current_node1 = self.head_node
            current_node2 = other.head_node
            while current_node1:
                if current_node1.value != current_node2.value:
                    return False
                else:
                    current_node1 = current_node1.next
                    current_node2 = current_node2.next
                return True
        return False

