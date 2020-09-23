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

    def empty(self):
        if self.head_node:
            return False
        return True
    
    def __bool__(self):
        return not self.head_node == None

    # Fill in the code for __len__
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

    def printQ(self):
        cur = self.head_node
        while(cur):
            print(cur.value)
            cur = cur.next

def inorder_to_postorder(exp):
    # create a queue to store our numbers
    num_queue = Queue()
    # create a queue to store our operands
    op_queue = Queue()

    # itterate through exp enqueuing numbers to num_stack
    # and operators to op_stack
    for char in exp:
        if char.isdigit():
            num_queue.enqueue(char)
        else:
            op_queue.enqueue(char)
    # post_exp will be our postfix expression
    post_exp = ""
    # itterate through both queues appeding the values to post_exp
    while num_queue:
        post_exp += num_queue.dequeue()
    while op_queue:
        post_exp += op_queue.dequeue()
    return post_exp


print(inorder_to_postorder("1-2/3+4"))
print(inorder_to_postorder("1+2*3"))




