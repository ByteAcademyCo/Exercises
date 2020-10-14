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


def minimum_parentheses(pstr):
    # use a stack to keep track of open parentheses
    stack = Stack()
    # keep track of num parentheses you need to add.
    num_paren = 0

    # loop through the parentheses in pstr
    for p in pstr:
        # push open parentheses onto your stack
        if p == '(':
            stack.push(p)
        # if p is ')' and we have an open parenthese for it to match with
        # pop an open parenthese off the stack
        elif stack:
                stack.pop()
        # otherwise we need to add an open parenthese to pstr before p.
        else:
            num_paren += 1
    # after itterating through the string we need to check if we have
    # any remaining opening parentheses in the stack we didn't have
    # a matching close parenthese for
    while stack:
        num_paren += 1
        stack.pop()
    return num_paren

pstr = "()))(("
print(minimum_parentheses(pstr))

pstr = "(("
print(minimum_parentheses(pstr))

pstr = "(()())"
print(minimum_parentheses(pstr))


    