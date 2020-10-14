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



def apply(operator, arg1, arg2):
    if operator == '+':
        return arg1 + arg2
    elif operator == '-':
        return arg1 - arg2
    elif operator == '*':
        return arg1 * arg2
    elif operator == '/':
        return arg1 / arg2

def postfix_eval(exp):
    # use a queue to keep track of operands
    queue = Queue()
    # ret_val will contain the evaluated expression
    ret_val = 0
    operator = None

    i = 0
    # loop through the digits in exp and add it to our queue
    while i < len(exp) and exp[i].isdigit():
        queue.enqueue(int(exp[i]))
        i += 1
    queue.printQ()
    # if our queue is not empty, assign the first number to ret_val
    if queue:
        ret_val = queue.dequeue()
    # we now hit the operators in exp, so we get the first
    # operator and apply it to our first two digits
    if i < len(exp):
        operator = exp[i]
        arg2 = queue.dequeue()
        ret_val = apply(operator, ret_val, arg2)
    # we increment i to move to the next operator
    i += 1
    while i < len(exp):
        # get the next operator 
        operator = exp[i]
        # get the next number from the queue for our argument
        arg2 = queue.dequeue()
        # update ret_val by applying the operator to 
        # ret_val and the new argument
        ret_val = apply(operator, ret_val, arg2)
        i += 1 
    return ret_val

exp = "123+*"
print(postfix_eval(exp))

exp = "1224+*/"
print(postfix_eval(exp))

print(postfix_eval(""))

    


    
