class ListNode:
  def __init__(self, value):
      self.value = value
      self.next = None

class Stack:
    def __init__(self):
        self.head_node = None

    def push(self, value):
        new_head = ListNode(value)
        new_head.next = self.head_node
        self.head_node = new_head

    def pop(self):
        if self.head_node:
            value = self.head_node.value
            self.head_node = self.head_node.next
            return value
        else:
            raise IndexError

    # Fill in the code for __len__
    def __len__(self):
        current_node = self.head_node
        number_nodes = 0
        while current_node:
            number_nodes += 1
            current_node = current_node.next
        return number_nodes