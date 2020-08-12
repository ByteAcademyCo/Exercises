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
    
    def __bool__(self):
        return not self.head_node == None
    
    def __len__(self):
        cur_node = self.head_node
        num_nodes = 0
        while(cur_node):
            num_nodes += 1
            cur_node = cur_node.next
        return num_nodes

    def __eq__(self, other):
        if(len(self) == len(other)):
            cur_node1 = self.head_node
            cur_node2 = other.head_node
            while(cur_node1):
                if not cur_node1.value == cur_node2.value:
                    return False
                else:
                    cur_node1 = cur_node1.next
                    cur_node2 = cur_node2.next
            return True
        return False


def backspace_compare(str1, str2):
    stack1 = Stack()
    stack2 = Stack()
    for char in str1:
        if(char == "#"):
            if (stack1):
                stack1.pop()
        else:
            stack1.push(char)
    for char in str2:
        if(char == "#"):
            if (stack2):
                stack2.pop()
        else:
            stack2.push(char)
    return stack1 == stack2
    