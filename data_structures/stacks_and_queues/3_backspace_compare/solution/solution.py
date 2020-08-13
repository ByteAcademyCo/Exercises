# def backspace_compare(str1=str, str2=str):
#     def New_string(string):
#         stack = []
#         for char in string:
#             if char != '#':
#                 stack.append(char)
#             elif stack:
#                 stack.pop()
#         return stack
#     return New_string(str1) == New_string(str2)

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
    # def __bool__(self):
    #     if self.head_node is None:
    #         return False
    #     else:
    #         return True
    def __len__(self):
        current_node = self.head_node
        number_nodes = 0
        while current_node:
            number_nodes += 1
            current_node = current_node.next
        return number_nodes
    def __eq__(self, other):
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

def backspace_compare(str1, str2):
    stack_1 = Stack()
    stack_2 = Stack()
    for char in str1:
        if char == '#':
            if stack_1:
                stack_1.pop()
        else:
            stack_1.push(char)
    for char in str2:
        if char == '#':
            if stack_2:
                stack_2.pop()
        else:
            stack_2.push(char)
    return stack_1 == stack_2