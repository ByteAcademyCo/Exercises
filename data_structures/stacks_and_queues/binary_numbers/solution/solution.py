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


def binary_numbers(n):
    # use a queue to keep track of previous binary numbers
    queue = Queue()
    # add '1' to our queue are the first binary number
    queue.enqueue('1')
    bin_lst = []
    for i in range(n):
        bin_val = queue.dequeue()
        bin_lst.append(bin_val)
        queue.enqueue(bin_val+'0')
        queue.enqueue(bin_val+'1')
    return bin_lst

print(binary_numbers(1))


   

    


    
